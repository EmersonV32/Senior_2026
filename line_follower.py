#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait, StopWatch, DataLog
m2 = Motor(Port.B)
m3 = Motor(Port.C)
csR = ColorSensor(Port.S1)
csL = ColorSensor(Port.S4)

def pid_line_follower(follow_sensor, stop_sensor,
                      motor_right, motor_left, base_speed,
                      Kp, Kd,
                      Ki = 0,
                      target=48.5,
                      max_angle=None,
                      stop_mode="c",
                      stop_threshold=20,
                      side="l"): 
    integral = 0
    last_error = 0

    motor_right.reset_angle(0)
    motor_left.reset_angle(0)

    while True:
        reflection = follow_sensor.reflection()
        stop_reflection = stop_sensor.reflection()

        # Stop condition
        if stop_mode == "c":
            if stop_reflection < stop_threshold:
                break
        elif stop_mode == "a":
            if max_angle is not None:
                if abs(motor_right.angle()) >= max_angle or abs(motor_left.angle()) >= max_angle:
                    break

        # Calculate error based on side
        if side == "l":
            error = reflection - target
        elif side == "r":
            error = target - reflection
        else:
            error = target - reflection

        integral += error
        derivative = error - last_error
        turn = Kp * error + Ki * integral + Kd * derivative

        right_speed = base_speed + turn
        left_speed = base_speed - turn

        motor_right.run(-right_speed)
        motor_left.run(left_speed)

        last_error = error
        wait(10)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    ev3.speaker.beep()  