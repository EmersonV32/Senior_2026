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

# your motors and sensors here
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)

# connect to slave
SLAVE_IP = '198.168.0.1'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SLAVE_IP, 9999))
ev3.speaker.beep()  # connected

# do your stuff here, then when you want slave motor A to move:
client.send(b'RUN')

client.close()
'''