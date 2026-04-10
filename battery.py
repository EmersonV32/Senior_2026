#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 brick
ev3 = EV3Brick()

from pybricks.hubs import EV3Brick

ev3 = EV3Brick()

volts = ev3.battery.voltage() / 1000

# Approximate percentage (for AA batteries: 7.2V full, 6V low)
percentage = int((volts - 6.0) / (7.2 - 6.0) * 100)
percentage = max(0, min(100, percentage))  # clamp 0-100%

ev3.screen.clear()
ev3.screen.print("Battery: {}%".format(percentage))