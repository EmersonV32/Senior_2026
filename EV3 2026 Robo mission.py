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

'''# Move 360 degrees (1 full rotation)
motor_d.run(500)
# Wait 1 second (1000 milliseconds)
wait(1000)
# Move 360 degrees (1 full rotation)
motor_a.run_angle(-1000, 250)
# Stop Motor D after
motor_d.stop()
motor_d.run_angle(-300, 140)
# Wait 1 second (1000 milliseconds)
wait(1000)
motor_a.run_angle(600, 270)

wait(1000)
motor_d.run(500)
wait(1000)
motor_a.run_angle(-1000, 270)
wait(1000)
motor_d.stop()
motor_d.run_angle(-300, 140)
wait(1000)
motor_a.run_angle(600, 270)

wait(1000)
motor_a.run_angle(-1000, 270)
wait(1000)
motor_d.run(500)
wait(1000)
motor_d.stop()
motor_a.run_angle(600, 270)
motor_d.run_angle(-300, 140)
wait(1000)'''


# Reset motor angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)
wait(50)  # छोट pause to stabilize motors
# ===== Helper: Move motors =====
def move_motors(left_speed, right_speed, duration_ms=None, rotations=None):
    if duration_ms is not None:
        left_motor.run_time(left_speed, duration_ms, Stop.BRAKE, wait=False)
        right_motor.run_time(right_speed, duration_ms, Stop.BRAKE, wait=True)

    elif rotations is not None:
        angle = 360 * rotations
        left_motor.run_angle(left_speed, angle, Stop.BRAKE, wait=False)
        right_motor.run_angle(right_speed, angle, Stop.BRAKE, wait=True)

# ===== Helper: Move until reflection condition =====
def move_until_reflect_condition(left_speed, right_speed, 
                                 sensor_port=Port.S4,
                                 threshold=30, condition="below",
                                 timeout=4000):

    color_sensor = ColorSensor(sensor_port)
    timer = StopWatch()

    left_motor.run(left_speed)
    right_motor.run(right_speed)

    while True:
        reflected = color_sensor.reflection()
        print("Reflected:", reflected)

        if condition == "above" and reflected >= threshold:
            break
        elif condition == "below" and reflected <= threshold:
            break

        # 🔥 Safety timeout (important for WRO)
        if timer.time() > timeout:
            print("Timeout reached")
            break

        wait(10)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    ev3.speaker.beep()

# ===== Helper: Line following with stop sensor =====
def move_motors_line_follow(left_speed, right_speed, 
                            line_sensor_port=Port.S4, 
                            stop_sensor_port=Port.S1,
                            Kp=4, midpoint=30, 
                            stop_threshold=20,
                            timeout=6000):

    line_sensor = ColorSensor(line_sensor_port)
    stop_sensor = ColorSensor(stop_sensor_port)
    timer = StopWatch()

    while True:
        line_val = line_sensor.reflection()
        stop_val = stop_sensor.reflection()

        print("Line:", line_val, "Stop:", stop_val)

        # Stop condition
        if stop_val < stop_threshold:
            print("Stop triggered")
            break

        # Safety timeout
        if timer.time() > timeout:
            print("Timeout reached")
            break

        # Proportional control
        error = line_val - midpoint
        turn = Kp * error

        left_motor.run(left_speed + turn)
        right_motor.run(right_speed + turn)

        wait(10)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    ev3.speaker.beep()

# ===== MAIN PROGRAM =====

motor_a.run_angle(-1000, 280)

# Turn
move_motors(500, -500, duration_ms=1000)
wait(100)

# Rotate
move_motors(-500, 500, rotations=1.25)

left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)

wait(500)

# Arm actions
motor_a.run_angle(600, 270)

motor_d.run(500)
wait(1000)
motor_d.stop()

motor_a.run_angle(-1000, 250)

# Small adjust
move_motors(-200, 200, rotations=0.4)

left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

# Motor D action
motor_d.run_angle(-300, 140)
wait(1000)

motor_a.run_angle(600, 270)

# Move forward
move_motors(-400, -400, rotations=0.8)

# Turn again
move_motors(500, -500, duration_ms=1000)

# Move until line detected
move_until_reflect_condition(
    left_speed=-400,
    right_speed=400,
    sensor_port=Port.S4,
    threshold=30,
    condition="below"
)

# Adjust + forward
move_motors(-200, 200, rotations=0.5)
move_motors(500, 500, rotations=0.7)

# Line follow
move_motors_line_follow(
    left_speed=-400,
    right_speed=400,
    line_sensor_port=Port.S1,
    stop_sensor_port=Port.S4
)

# Final moves
move_motors(-200, 200, rotations=0.2)
move_motors(-500, -500, rotations=0.8)

# Final line follow
move_motors_line_follow(
    left_speed=-400,
    right_speed=400,
    line_sensor_port=Port.S1,
    stop_sensor_port=Port.S4
)