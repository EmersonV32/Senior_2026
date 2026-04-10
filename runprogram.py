#!/usr/bin/env pybricks-micropython

# ===== Imports =====
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
from test_small import test_test

# ===== Initialize EV3 =====
ev3 = EV3Brick()
ev3.speaker.beep()

# ===== Motors =====
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)

# Reset angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)
motor_a.reset_angle(0)
motor_d.reset_angle(0)

wait(50)

test_test()
