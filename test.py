#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)

#Reset angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)
motor_a.reset_angle(0)
motor_d.reset_angle(0)

wait(50)

# ===== BASIC MOVEMENT FUNCTION =====
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


# ===== MAIN PROGRAM =====
motor_a.run_angle(-1000, 280) # moves the white thing up

move_motors(500, -500, duration_ms=1000) # aligns with the wall
wait(500)

move_motors(-300, 302, rotations=1.23) # moves to the first row of yellow blocks
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
wait(500)

motor_a.run_angle(600, 250) # move down the white thing to take first row of yellow blocks
wait(500)

motor_d.run(500) # holds the blocks in place
wait(1000)

motor_a.run_time(-1000, 1100)  # move up the white thing

move_motors(-100, 110, rotations=0.378) # moves to the second row of yellow blocks
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

motor_a.run_angle(200, 160) # moves the white thing down a little bit
wait(170)

motor_d.stop()
wait(50)

motor_a.run_time(350, 650, wait=False) # moves the white thing down

motor_d.run_time(-1000, 100.1) # releases the yellow block on top of the blue block
wait(250)

motor_a.run_time(50, 2500, wait=False) # moves the white thing down

counter = 0
while counter <= 6:
    move_motors(-100, -100, degrees=20)
    move_motors(100, 100, degrees=20)
    counter +=1
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

motor_d.run(500) # holds the block 
wait(200)

wait(100000000)
motor_a.run_time(-1000, 500) # moves the white thing up




'''
counter = 0
while counter <= 3:
    move_motors(-100, -200, degrees=15)
    move_motors(100, 200, degrees=15)
    counter +=1
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)
'''