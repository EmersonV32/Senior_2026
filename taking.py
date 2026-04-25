#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
from line_follower import pid_line_follower

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)
colorsensorLeft = ColorSensor(Port.S1)
colorsensorRight = ColorSensor(Port.S4)

#Reset angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)
motor_a.reset_angle(0)
motor_d.reset_angle(0)

wait(50)

# movement function (kind of like th epink blocks in ev3 classroom)
def move_motors(left_speed, right_speed, duration_ms=None, rotations=None, degrees=None):
    if duration_ms is not None:
        left_motor.run_time(left_speed, duration_ms, Stop.BRAKE, wait=False)
        right_motor.run_time(right_speed, duration_ms, Stop.BRAKE, wait=True)

    elif rotations is not None:
        angle = 360 * rotations
        left_motor.run_angle(left_speed, angle, Stop.BRAKE, wait=False)
        right_motor.run_angle(right_speed, angle, Stop.BRAKE, wait=True)
    
    elif degrees is not None:
        left_motor.run_angle(left_speed, degrees, Stop.BRAKE, wait=False)
        right_motor.run_angle(right_speed, degrees, Stop.BRAKE, wait=True)


# start of the program
def mozaic():
    move_motors(500, -500, duration_ms=850) # aligns with the wall
    wait(500)

    move_motors(-300, 302, rotations=1.19) # moves to the first row of yellow blocks
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(500)

    motor_a.run_angle(600, 260) # move down the white thing to take first row of yellow blocks
    wait(500)

    motor_d.run(500) # holds the blocks in place
    wait(100)

    motor_a.run_time(-1000, 900)  # move up the white thing

    move_motors(500,-500, rotations=0.1)

    move_motors(-500,-500, rotations=0.41) # turns to go deposit to the black grid
    wait(100)

    move_motors(-567, 575, rotations=3.35) 
    wait(100)

    while colorsensorLeft.reflection() > 30:
        left_motor.run(-350)
        right_motor.run(350)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(250)

    move_motors(-300, 300, rotations=0.4)
    wait(100)

    move_motors(-300, -300, rotations=0.3)
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S4,
                        stop_sensor_port=Port.S1,
                        base_speed=300,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="r")

    wait(100)
    move_motors(-200, 200, rotations=0.55)

    motor_a.run_angle(1000, 260) # moves the white thing down to deposit on black thing

    motor_d.stop()
    wait(50)

    motor_d.run_time(-300, 250) # releases the first row in the grid
    wait(250)

    motor_a.run_angle(-1000, 250) # moves the white thing up a little bit
    wait(250)