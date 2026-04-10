#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
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


# Initialize motors (adjust ports if needed)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize only Motor A
m1 = Motor(Port.A)
m2 = Motor(Port.B)
m3 = Motor(Port.C)
m4 = Motor(Port.D)
m1.reset_angle(0)
m2.reset_angle(0)
m3.reset_angle(0)
m4.reset_angle(0)

# Reset motor angles
m2.reset_angle(0)
m3.reset_angle(0)
wait(50)  # छोट pause to stabilize motors

def move_motors(ls, rs, duration=None, rotation=None):
    if duration is not None:
        left_motor.run_time(ls, duration, Stop.BRAKE, wait=False)
        right_motor.run_time(rs, duration, Stop.BRAKE, wait=True)
    elif rotation is not None:
        angle = 360 * rotation
        left_motor.run_angle(ls, angle, Stop.BRAKE, wait=False)
        right_motor.run_angle(rs, angle, Stop.BRAKE, wait=True)
    else:
        return  # safely exit if nothing provided

m1.run_angle(-1000, 280)





left_motor.reset_angle(0)
right_motor.reset_angle(0)

wait(100)  # IMPORTANT: pause between commands

# Second movement
move_motors(ls=-300, rs=300, rotation=1.25)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)

wait(500)
m1.run_angle(600, 250)# Move 360 degrees (1 full rotation)
wait(1000)
m4.run(300)
# Wait 1 second (1000 milliseconds)
wait(2000)
# Move 360 degrees (1 full rotation)
m1.run_angle(-1000, 265)

move_motors(left_speed=-200, right_speed=200, rotations=0.4)
m2.stop(Stop.COAST)
m3.stop(Stop.COAST)

m1.run_angle(200, 50)
# Stop Motor D after
m4.stop()
wait(50)
m4.run_angle(-300, 50)
# Wait 1 second (1000 milliseconds)
wait(2000)
move_motors(ls=-100, rs=100, rotation=0.1)
m1.run_angle(600, 250)
wait(1000)
m4.run(500)
# Wait 1 second (1000 milliseconds)
wait(2000)

wait(10000)