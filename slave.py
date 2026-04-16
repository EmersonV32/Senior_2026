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
    