#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import socket

ev3 = EV3Brick()
motor_a = Motor(Port.A)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(1)

ev3.speaker.beep()  # ready
conn, addr = server.accept()

data = conn.recv(64).decode()
if data == 'RUN':
    motor_a.run_angle(500, 360)

conn.close()
server.close()