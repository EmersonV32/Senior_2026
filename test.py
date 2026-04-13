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
csL = ColorSensor(Port.S1)

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

move_motors(500, -500, duration_ms=850) # aligns with the wall
wait(500)

move_motors(-300, 302, rotations=1.23) # moves to the first row of yellow blocks
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
wait(500)

motor_a.run_angle(600, 250) # move down the white thing to take first row of yellow blocks
wait(500)

motor_d.run(500) # holds the blocks in place
wait(1000)

motor_a.run_time(-1000, 900)  # move up the white thing

move_motors(-100, 100, rotations=0.385) # moves to the second row of yellow blocks
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

motor_a.run_angle(200, 120) # moves the white thing down a little bit
wait(170)

motor_d.stop()
wait(50)

#motor_a.run_time(200, 900) # moves the white thing down

motor_d.run_time(-300, 250) # releases the first row of yellow block on top of the second row 
wait(250)

motor_a.run_time(100, 1200, wait=False) # moves the white thing down
wait(400)

counter = 0
while counter <= 3:
    move_motors(-100, -100, degrees=10)
    move_motors(100, 100, degrees=10)
    counter +=1
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)


motor_d.run(500) # holds the block 
wait(200)

motor_a.run_angle(-1000, 200) # moves the white thing up

left_motor.run_angle(-500,380) 

move_motors(-500, 520, rotations=1.95) 
wait(100)

while csL.reflection() > 30:
    left_motor.run(-500)
    right_motor.run(500)

left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
wait(100)

move_motors(-200, 200, rotations=0.1)
wait(100)

left_motor.run_angle(-400, 150)

pid_line_follower(follow_sensor_port=Port.S1,
                      stop_sensor_port=Port.S4,
                      base_speed=250,
                      Kp=2.5, Kd=3, Ki=0,
                      target=50,
                      max_angle=None,
                      stop_mode="c",
                      stop_threshold=20,
                      side="l")


wait(100)
move_motors(-200, 200, rotations=0.85)

motor_a.run_angle(1000, 200) # moves the white thing down to deposit on black thing
wait(100)

motor_d.stop()
wait(50)

motor_d.run_time(-300, 250) # releases the first row in the grid
wait(100)

motor_a.run_angle(-1000, 50) # mmoves the white thing up a little bit 
wait(100)

motor_d.run(500) # holds the blocks in place
wait(100)

move_motors(100, -100, degrees=360)
wait(100)





wait(10000)








'''
counter = 0
while counter <= 3:
    move_motors(-100, -200, degrees=15)
    move_motors(100, 200, degrees=15)
    counter +=1
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)
'''



'''
#putting the blocks in the black grid
motor_d.run(500) # holds the blocks in place
wait(1000)

motor_a.run_angle(-1000, 280) # moves the white thing up

move_motors(-300, 300, rotations=0.85)

motor_a.run_angle(600, 250) # move down the white thing to take first row of yellow blocks

motor_d.stop()
wait(50)

motor_d.run_time(-1000, 200) # releases the yellow block on top of the blue block

motor_a.run_angle(-1000, 160) # moves the white thing up

wait(2000)

counter = 0
while counter <= 3:
    move_motors(-100, -100, degrees=20)
    move_motors(100, 100, degrees=20)
    wait(100)
    counter +=1
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

move_motors(-100, -100, degrees=20)
move_motors(100, 100, degrees=30)

wait(100)

motor_a.run_angle(-1000, 110) # moves the white thing up


wait(100000)
'''