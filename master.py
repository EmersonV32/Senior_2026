#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import socket

ev3 = EV3Brick()

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