#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)
colorsensorLeft = ColorSensor(Port.S1)
colorsensorRight = ColorSensor(Port.S4)

left_motor.reset_angle(0)
right_motor.reset_angle(0)
motor_a.reset_angle(0)
motor_d.reset_angle(0)