#!/usr/bin/env pybricks-micropython

# ===== Imports =====
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch

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

'''
# ===== BASIC MOVEMENT FUNCTION =====
def move_motors(left_speed, right_speed, duration_ms=None, rotations=None):
    if duration_ms is not None:
        left_motor.run_time(left_speed, duration_ms, Stop.BRAKE, wait=False)
        right_motor.run_time(right_speed, duration_ms, Stop.BRAKE, wait=True)

    elif rotations is not None:
        angle = 360 * rotations
        left_motor.run_angle(left_speed, angle, Stop.BRAKE, wait=False)
        right_motor.run_angle(right_speed, angle, Stop.BRAKE, wait=True)

# ===== MOVE UNTIL COLOR CONDITION =====
def move_until_reflect_condition(left_speed, right_speed, 
                                 sensor_port=Port.S4,
                                 threshold=30, condition="below"):

    sensor = ColorSensor(sensor_port)

    left_motor.run(left_speed)
    right_motor.run(right_speed)

    while True:
        value = sensor.reflection()

        if condition == "below" and value <= threshold:
            break
        elif condition == "above" and value >= threshold:
            break

        wait(10)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    ev3.speaker.beep()

# ===== PID LINE FOLLOWER =====
def pid_line_follower(follow_sensor_port=Port.S1,
                      stop_sensor_port=Port.S4,
                      base_speed=400,
                      Kp=2, Kd=3, Ki=0,
                      target=30,
                      max_angle=None,
                      stop_mode="c",
                      stop_threshold=20,
                      side="r"):

    follow_sensor = ColorSensor(follow_sensor_port)
    stop_sensor = ColorSensor(stop_sensor_port)

    integral = 0
    last_error = 0

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

    while True:
        reflection = follow_sensor.reflection()
        stop_reflection = stop_sensor.reflection()

        # ===== STOP CONDITIONS =====
        if stop_mode == "c":
            if stop_reflection < stop_threshold:
                break

        elif stop_mode == "a":
            if max_angle is not None:
                if abs(left_motor.angle()) >= max_angle or abs(right_motor.angle()) >= max_angle:
                    break

        # ===== PID CALCULATION =====
        if side == "l":
            error = reflection - target
        else:
            error = target - reflection

        integral += error
        derivative = error - last_error

        turn = Kp * error + Ki * integral + Kd * derivative

        right_speed = base_speed + turn
        left_speed = base_speed - turn

        # Clamp speeds (safety)
        right_speed = max(min(right_speed, 1000), -1000)
        left_speed = max(min(left_speed, 1000), -1000)

        # Motor directions (your setup)
        left_motor.run(-left_speed)
        right_motor.run(right_speed)

        last_error = error
        wait(10)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    ev3.speaker.beep()
'''

def test_test():
    wait(1000)
    motor_d.run_time(500, 500)
    # Wait 1 second (1000 milliseconds)
    wait(2000)
    # Move 360 degrees (1 full rotation)
    motor_a.run_angle(-1000, 270)
