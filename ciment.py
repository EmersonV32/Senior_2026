#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
import usocket as socket
from line_follower import pid_line_follower
from taking import move_motors
from config import ev3, left_motor, right_motor, motor_a, motor_d, colorsensorLeft, colorsensorRight


def send_cmd(sock, cmd):
    sock.send((cmd + "\n").encode())

def done(sock):
    send_cmd(sock, "done")
    sock.close()

def tool3(sock):
    move_motors(-350, 350, rotations=0.5)
    wait(250)

    move_motors(350, 350, rotations=0.35)
    wait(250)

    move_motors(-450, 450, rotations=1.8)

    while colorsensorRight.reflection() > 30:
        left_motor.run(-350)
        right_motor.run(350)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

    move_motors(-350, 350, rotations=0.15)

    move_motors(-350, -350, rotations=0.35)
    wait(100)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=369,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")
    wait(100)

    move_motors(500, -500, rotations=0.35)
    wait(200)

    move_motors(-500, -500, rotations=1.53)
    wait(250)

    move_motors(500, -500, rotations=0.34)

    send_cmd(sock,"T, 450, 480") # turns down the motor A
    wait(500)

    move_motors(200, 200, rotations=0.2)
    move_motors(-200, -200, rotations=0.2)
    wait(350)

    right_motor.run_angle(450, 470)
    wait(250)
    
    move_motors(-607, 607, rotations=3.7)

    move_motors(-450, -450, rotations=0.6)
    wait(250)

    move_motors(-400, 400, rotations=0.2)

    pid_line_follower(follow_sensor_port=Port.S4,
                        stop_sensor_port=Port.S1,
                        base_speed=500,
                        Kp=2.5, Kd=3, Ki=0,
                        target=47,
                        max_angle=950,
                        stop_mode="a",
                        stop_threshold=22,
                        side="l")

    pid_line_follower(follow_sensor_port=Port.S4,
                        stop_sensor_port=Port.S1,
                        base_speed=500,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")
    wait(100)

    move_motors(-450, 450, rotations=0.7)
    wait(100)

    left_motor.run_angle(500, 530)
    wait(250)

    move_motors(400, -400, rotations=0.25)

    send_cmd(sock, "T,-750, 400") # turns up the motor A
    wait(500)

    move_motors(-400, 400, rotations=1.1)
    wait(100)

    move_motors(-500, -500, rotations=0.76)
    wait(100)

    right_motor.run_angle(400,100)
    left_motor.run_angle(-400, 100)
    wait(100)

    move_motors(-500, 500, rotations=2.2)
    wait(100)

    move_motors(600, -635, rotations=3.7)
    wait(100)

    send_cmd(sock, "T, 750, 600")
    wait(650)

    move_motors(-1000, 900, rotations=6.2)
    wait(100)

    move_motors(900, 900, rotations=2)

    move_motors(500, -500, rotations=1)