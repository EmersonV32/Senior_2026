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
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_d = Motor(Port.D)
motor_a.reset_angle(0)
motor_b.reset_angle(0)
motor_c.reset_angle(0)
motor_d.reset_angle(0)



# Reset motor angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)
wait(50)  # छोट pause to stabilize motors

def move_motors(left_speed, right_speed, duration_ms=None, rotations=None):
    if duration_ms is not None:
        left_motor.run_time(left_speed, duration_ms, Stop.BRAKE, wait=False)
        right_motor.run_time(right_speed, duration_ms, Stop.BRAKE, wait=True)
    elif rotations is not None:
        angle = 360 * rotations
        left_motor.run_angle(left_speed, angle, Stop.BRAKE, wait=False)
        right_motor.run_angle(right_speed, angle, Stop.BRAKE, wait=True)
    else:
        return  # safely exit if nothing provided

'''motor_a.run_angle(600, 250)# Move 360 degrees (1 full rotation)
wait(1000)
motor_d.run(300)
# Wait 1 second (1000 milliseconds)
wait(2000)
# Move 360 degrees (1 full rotation)
motor_a.run_angle(-1000, 265)
wait(2000)
c
# Move 360 degrees (1 full rotation)
motor_a.run_angle(-1100, 275)
wait(2000)'''




motor_a.run_angle(-1000, 280)

# First movement
move_motors(left_speed=500, right_speed=-500, duration_ms=1000)

left_motor.reset_angle(0)
right_motor.reset_angle(0)

wait(100)  # IMPORTANT: pause between commands

# Second movement
move_motors(left_speed=-300, right_speed=300, rotations=1.21)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)

wait(500)
motor_a.run_angle(600, 250)# Move 360 degrees (1 full rotation)
wait(1000)
motor_d.run(300)
# Wait 1 second (1000 milliseconds)
wait(2000)
# Move 360 degrees (1 full rotation)
motor_a.run_angle(-1000, 270)

move_motors(left_speed=-200, right_speed=200, rotations=0.3)
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

motor_a.run_angle(200, 50)
# Stop Motor D after
motor_d.stop()
wait(50)
motor_d.run_angle(-300, 50)
# Wait 1 second (1000 milliseconds)
wait(2000)
move_motors(left_speed=-100, right_speed=100, rotations=0.1)
motor_a.run_angle(600, 250)
wait(1000)
motor_d.run(500)
# Wait 1 second (1000 milliseconds)
wait(2000)

wait(10000)

move_motors(left_speed=-400, right_speed=-400, rotations=0.8)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
move_motors(left_speed=500, right_speed=-500, duration_ms=1000)

wait(10000)

def move_until_reflect_condition(left_speed, right_speed, 
                                 sensor_port=Port.S4,
                                 threshold=30, condition="above"):
    """
    Moves motors until the color sensor meets a condition.

    Parameters:
    - left_speed, right_speed: motor speeds
    - sensor_port: which port the color sensor is on
    - threshold: reflection value to trigger stop
    - condition: "above" or "below"
    """
    
    # Initialize sensor INSIDE the function (so it's adjustable)
    color_sensor = ColorSensor(sensor_port)

    # Start motors
    left_motor.run(left_speed)
    right_motor.run(right_speed)

    while True:
        reflected = color_sensor.reflection()
        print("Reflected light:", reflected)
        
        if condition == "above" and reflected >= threshold:
            break
        elif condition == "below" and reflected <= threshold:
            break
        
        wait(10)

    # Stop motors
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    ev3.speaker.beep()
# move forward until reflection is below 30
move_until_reflect_condition(
    left_speed=-400,
    right_speed=400,
    sensor_port=Port.S4,
    threshold=30,
    condition="below"
)
move_motors(left_speed=-200, right_speed=200, rotations=0.5)
move_motors(left_speed=500, right_speed=500, rotations=0.7)

# Function: move motors with optional line-following until stop sensor triggers
def move_motors_line_follow(left_speed, right_speed, 
                            line_sensor_port=Port.S4, stop_sensor_port=Port.S1,
                            base_speed=400, Kp=4, midpoint=30, stop_threshold=20):
    """
    Moves the robot following a line with one sensor, stops when stop_sensor sees reflection < stop_threshold.
    
    Parameters:
    - left_speed: base speed for left motor (negative for forward)
    - right_speed: base speed for right motor (positive for forward)
    - line_sensor_port: Port of the line-following color sensor
    - stop_sensor_port: Port of the stop color sensor
    - base_speed: base speed for line following
    - Kp: proportional gain for line correction
    - midpoint: expected reflection midpoint of line vs floor
    - stop_threshold: stop when stop sensor sees reflection < stop_threshold
    """
    
    line_sensor = ColorSensor(line_sensor_port)
    stop_sensor = ColorSensor(stop_sensor_port)
    
    print("Starting line following until stop sensor triggers...")
    
    while True:
        line_reflection = line_sensor.reflection()
        stop_reflection = stop_sensor.reflection()
        
        print("Line:", line_reflection, "Stop:", stop_reflection)  # debug
        
        # Stop condition
        if stop_reflection < stop_threshold:
            left_motor.stop(Stop.BRAKE)
            right_motor.stop(Stop.BRAKE)
            ev3.speaker.beep()
            print("Stop sensor triggered, stopping.")
            break
        
        # Proportional control
        error = line_reflection - midpoint
        turn = Kp * error
        
        # Adjusted for left motor negative, right motor positive
        left_motor.run(left_speed + turn)   # left motor is negative for forward
        right_motor.run(right_speed + turn) # right motor positive for forward
        
        wait(10)

move_motors_line_follow(
    left_speed=-400,    # left motor negative = forward
    right_speed=400,    # right motor positive = forward
    line_sensor_port=Port.S1,  # line follower sensor
    stop_sensor_port=Port.S4,  # stop sensor
    base_speed=400,     # adjust speed if needed
    Kp=4,               # adjust turning sensitivity
    midpoint=30,        # adjust depending on track colors
    stop_threshold=20   # stop when stop sensor sees reflection <20
)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)

move_motors(left_speed=-200, right_speed=200, rotations=0.2)
move_motors(left_speed=-500, right_speed=-500, rotations=0.8)

move_motors_line_follow(
    left_speed=-400,    # left motor negative = forward
    right_speed=400,    # right motor positive = forward
    line_sensor_port=Port.S1,  # line follower sensor
    stop_sensor_port=Port.S4,  # stop sensor
    base_speed=400,     # adjust speed if needed
    Kp=4,               # adjust turning sensitivity
    midpoint=30,        # adjust depending on track colors
    stop_threshold=20   # stop when stop sensor sees reflection <20
)