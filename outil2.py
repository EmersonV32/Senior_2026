#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait
import usocket as socket
from taking import  move_motors
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

def send_cmd(sock, cmd):
    sock.send((cmd + "\n").encode())

def done(sock):
    send_cmd(sock, "done")
    sock.close()

def tool2(sock):
    move_motors(-500, -500, rotations=0.745)
    wait(150)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=475,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=667,
                        stop_mode="a",
                        stop_threshold=22,
                        side="r")
    
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="r")
    
    wait(250)

    move_motors(-300, 300, rotations=0.2)
    wait(250)

    move_motors(300, 300, rotations=0.745)
    wait(250)

    send_cmd(sock,"T, 350, 450") # turns down the motor A
    wait(500)

    move_motors(-300, -300, rotations=0.745)
    wait(100)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=510,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=1075,
                        stop_mode="a",
                        stop_threshold=22,
                        side="r")

    wait(250)

    move_motors(500, 500, rotations=0.745)
    wait(100)

    move_motors(-500, 500, rotations=2.1)
    wait(100)

    send_cmd(sock, "T, -1000, 300")
    wait(300)

    ev3.speaker.beep()

