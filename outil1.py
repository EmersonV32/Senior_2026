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

def tool1():
    ev3.speaker.beep()
    sock = socket.socket()

    connected = False
    while not connected:
        try:
            ev3.screen.print("Linking to Slave...")
            sock.connect(socket.getaddrinfo('192.168.0.1', 12345)[0][-1])
            connected = True
        except OSError:
            ev3.screen.print("Retry in 1s...")
            wait(1000) 

    ev3.screen.print("Connected!")
    ev3.speaker.beep()

    move_motors(500, -500, rotations= 0.15) # moves back from the grid 

    move_motors(-500, -500, rotations= 1.485) # turns 180° 
    wait(500)

    send_cmd(sock, "T, 250, 500") # turns down the motor A
    wait(500)


    move_motors(-75, -75, degrees=30)
    wait(100)
    move_motors(75, 75, degrees=50)

    send_cmd(sock, "T,-1000, 500") # turns up the motor A
    wait(250)

    move_motors(-500, 500, rotations=1.5) 
    wait(100)

    move_motors(500, 500, rotations=0.75)
    wait(100)

    move_motors(-500, 500, rotations=1.85)
    wait(100)

    while colorsensorLeft.reflection() > 30:
        left_motor.run(-500)
        right_motor.run(500)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(100)

    move_motors(-500, 500, rotations=0.15)
    wait(100)

    move_motors(-500, -500, rotations=0.75)
    wait(100)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="l")
    wait(100)

    move_motors(-500, 500, rotations=0.15)
    wait(100)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")

    wait(125)

    move_motors(-500, 500, rotations=0.967)
    wait(100)

    move_motors(-500, -500, rotations=0.745)
    wait(250)

    move_motors(-250, 250, rotations=0.44)
    wait(250)

    motor_a.run_angle(600, 260)
    wait(250)

    motor_d.run(500) # holds the blocks in place
    wait(100)

    motor_a.run_time(-1000, 900)
    wait(250)

    move_motors(500, -500, rotations=0.55)
    wait(100)

    move_motors(-500, -500, roations=0.745)
    wait(100)

    move_motors(-500, 500, rotations=0.55)
    wait(100)


    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=350,
                        Kp=2, Kd=2, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="r")
    
    wait(250)

    move_motors(-300, 300, rotations=0.15)
    wait(100)

    move_motors(500, 500, rotations=0.745)
    wait(100)

    send_cmd(sock, "T, 500, 250")
    wait(249)

    move_motors(-500, -500, rotations=0.745)
    wait(150)

    move_motors(500, -500, rotations=1.4)
    wait(150)

    move_motors(500, 500, rotations=0.745)
    wait(150)

    send_cmd(sock, "T, -750, 150")
    wait()




    

        

    done(sock)