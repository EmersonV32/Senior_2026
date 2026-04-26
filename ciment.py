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

def test3(sock):
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
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=369,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")
    wait(250)

    move_motors(500, -500, rotations=0.3)
    wait(200)

    move_motors(-500, -500, rotations=1.53)
    wait(250)

    move_motors(500, -500, rotations=0.3)

    send_cmd(sock,"T, 450, 480") # turns down the motor A
    wait(500)

    move_motors(200, 200, rotations=0.2)
    move_motors(-200, -200, rotations=0.2)
    wait(350)

    right_motor.run_angle(505, 470)
    wait(250)

    move_motors(-607, 607, rotations=3.8)
    wait(250)

    move_motors(-450, -450, rotations=0.6)
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S4,
                        stop_sensor_port=Port.S1,
                        base_speed=500,
                        Kp=3, Kd=3, Ki=0,
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
    wait(250)

    move_motors(-450, 450, rotations=0.75)
    wait(250)

    left_motor.run_angle(500, 520)
    wait(250)

    move_motors(300, -300, rotations=0.35)
    wait(250)

    move_motors(-300, 300, rotations=0.15)
    wait(250)

    send_cmd(sock, "T,-750, 500") # turns up the motor A
    wait(500)

    motor_d.run_time(200, 500, wait=False)

    move_motors(-400, 400, rotations=0.6)
    wait(250)

    motor_d.stop(Stop.BRAKE)
    wait(50)

    move_motors(400, 400, rotations=0.55)
    wait(150)
    
    move_motors(-369, 369, rotations=1.1)
    wait(150)

    motor_a.run_angle(600, 175) # move down the white thing to take first row of yellow blocks
    wait(100)

    move_motors(250, 250, rotations=1.67)
    wait(100)

    move_motors(-350, 350, rotations=2.9)
    wait(150)

    move_motors()









def aroundgrid(sock):
    move_motors(500, -500, rotations=1.65)
    wait(250)

    send_cmd(sock, "T, 100, 100")
    wait(150)

    move_motors(250, 250, rotations=1.49)
    wait(250) 

    move_motors(400, -400, rotations=0.8)
    wait(250)

    move_motors(-400, -400, rotations=0.3)
    wait(250)

    move_motors(400, -400, rotations=1.15)
    wait(250)

    send_cmd(sock, "T,-500, 450") # turns up the motor A
    wait(250)

    move_motors(-400, 400, rotations=1.15)
    wait(250)

    move_motors(400, 400, rotations=0.3)
    wait(250)

    move_motors(400, -400, rotations=0.5)
    wait(250)

    send_cmd(sock, "T, 250, 480") # turns down the motor A
    wait(500)

    move_motors(-75, -75, degrees=30)  # twists to put the blocks in the black grid
    wait(250)
    move_motors(75, 75, degrees=40) # twists to put the blocks in the black grid

    send_cmd(sock, "T,-1000, 500") # turns up the motor A
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=500,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=950,
                        stop_mode="a",
                        stop_threshold=22,
                        side="l")
    
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=300,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")

    wait(250)

    move_motors(500, -500, rotations=0.2)
    wait(200)

    move_motors(-500, -500, rotations=1.49)
    wait(250)

    move_motors(500, -500, rotations=0.25)

    send_cmd(sock,"T, 500, 480") # turns down the motor A
    wait(500)

    move_motors(200, 200, rotations=0.2)
    move_motors(-200, -200, rotations=0.2)
    wait(350)

    pid_line_follower(follow_sensor_port=Port.S4,
                        stop_sensor_port=Port.S1,
                        base_speed=500,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=950,
                        stop_mode="a",
                        stop_threshold=22,
                        side="r")
    
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S4,
                        stop_sensor_port=Port.S1,
                        base_speed=300,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="r")
    wait(250)

    move_motors(500, -500, rotations=1.05)
    wait(250)

    move_motors(250, 250, rotations=1.49)
    wait(250) 

    move_motors(400, -400, rotations=0.85)
    wait(250)

    send_cmd(sock, "T,-250, 500")
    wait(500)

    ev3.speaker.beep()

    return sock