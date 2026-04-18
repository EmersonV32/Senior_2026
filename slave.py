#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import usocket as socket

ev3 = EV3Brick()
motor_a = Motor(Port.A)

server = socket.socket()
server.bind(socket.getaddrinfo('0.0.0.0', 12345)[0][-1])
server.listen(1)

ev3.screen.print("Waiting...")
conn, addr = server.accept()
ev3.screen.print("Connected!")

while True:
    msg = conn.recv(64).decode().strip()
    
    if not msg or msg == "done":
        break

    parts = msg.split(",")
    mode = parts[0]
    speed = int(parts[1])
    value = int(parts[2])

    if mode == "A":
        motor_a.run_angle(speed, value)
    elif mode == "T":
        motor_a.run_time(speed, value)

conn.close()
server.close()
























'''
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import usocket as socket

ev3 = EV3Brick()

def send_cmd(sock, cmd):
    sock.send((cmd + "\n").encode())

def done(sock):
    send_cmd(sock, "done")
    sock.close()

sock = socket.socket()
sock.connect(socket.getaddrinfo('192.168.0.1', 12345)[0][-1])

send_cmd(sock, "A,500,360")
wait(1000)

done(sock)
'''