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

def test1():
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

    send_cmd(sock, "T, 250, 400") # turns down the motor A
    wait(500)

    move_motors(-75, -75, degrees=30)  # twists to put the blocks in the black grid
    wait(250)
    move_motors(75, 75, degrees=50) # twists to put the blocks in the black grid

    move_motors(-300, 300, rotations=0.2)

    send_cmd(sock, "T,-1000, 500") # turns up the motor A
    wait(150)

    move_motors(-500, 500, rotations=1.47) # moves to go and get the second row
    wait(150)

    move_motors(500, 500, rotations=0.75) # moves to go and get the second row
    wait(150)

    move_motors(-500, 500, rotations=1.9) # moves to go and get the second row
    wait(150)

    while colorsensorLeft.reflection() > 30:   # moves to go and get the second row
        left_motor.run(-300)
        right_motor.run(300)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(250)

    move_motors(-300, 300, rotations=0.12)   # moves to go and get the second row
    wait(150)

    move_motors(-500, -500, rotations=0.75)   # moves to go and get the second row
    wait(150)

    pid_line_follower(follow_sensor_port=Port.S1,   # moves to go and get the second row
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="l")
    wait(250)

    move_motors(-350, 350, rotations=0.15)  # moves to go and get the second row
    wait(150)

    pid_line_follower(follow_sensor_port=Port.S1,   # moves to go and get the second row
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")

    wait(250)

    move_motors(-300, 300, rotations=0.95) # moves to go and get the second row
    wait(250)

    move_motors(-300, -300, rotations=0.75) # moves to go and get the second row
    wait(250)

    move_motors(-300, 300, rotations=0.42) # moves to go and get the second row
    wait(250)

    motor_a.run_angle(600, 260) # moves down the 3d print with the second row
    wait(250)

    motor_d.run(500) # holds the blocks in place
    wait(150)

    motor_a.run_time(-1000, 850) # moves up the 3d print with the second row
    wait(250)

    move_motors(500, -500, rotations=0.55) # goes to take the first tool, bowl
    wait(150)

    move_motors(-500, -500, rotations=0.745)
    wait(150)

    move_motors(-500, 500, rotations=0.9)
    wait(250)


    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=500,
                        Kp=2, Kd=2, Ki=0,
                        target=47,
                        max_angle=1150,
                        stop_mode="a",
                        stop_threshold=20,
                        side="r")
    
    wait(250)
    
    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=400,
                        Kp=2, Kd=2, Ki=0,
                        target=47,
                        max_angle=500,
                        stop_mode="c",
                        stop_threshold=20,
                        side="r")
    
    wait(350)

    move_motors(-300, 300, rotations=0.2)
    wait(250)

    move_motors(450, 450, rotations=0.745)
    wait(250)

    send_cmd(sock,"T, 506, 450") # turns down the motor A
    wait(500)

    move_motors(-450, -450, rotations=0.745)
    wait(100)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=600,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=1120,
                        stop_mode="a",
                        stop_threshold=22,
                        side="r")
    
    wait(350)

    move_motors(250, 250, rotations=0.75)
    wait(100)

    move_motors(-500, 500, rotations=1.75)
    wait(100)

    move_motors(350, -350, rotations=0.2)
    wait(250)

    send_cmd(sock,"T, -250, 480") # turns up the motor A
    wait(500)

    move_motors(-500, 500, rotations=0.7)

    while colorsensorLeft.reflection() > 30:
        left_motor.run(-350)
        right_motor.run(350)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(250)

    move_motors(-350, 350, rotations=0.15)
    wait(250)

    move_motors(400, 400, rotations=0.745)
    wait(250)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=400,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")
    wait(250)

    move_motors(-200, 200, rotations=0.55)

    motor_a.run_angle(1000, 250) # moves the white thing down to deposit on black thing
    wait(100)

    motor_d.stop()
    wait(50)

    motor_d.run_time(-300, 250) # releases the first row in the grid
    wait(250)

    motor_a.run_angle(-1000, 250) # moves the white thing up a little bit
    wait(250)

    move_motors(500, -500, rotations= 0.2) # moves back from the grid 

    move_motors(-500, -500, rotations= 1.485) # turns 180° 

    send_cmd(sock, "T, 250, 400") # turns down the motor A
    wait(500)

    move_motors(-75, -75, degrees=30)  # twists to put the blocks in the black grid
    wait(250)
    move_motors(75, 75, degrees=40) # twists to put the blocks in the black grid

    move_motors(-250, 250, rotations=0.2)

    send_cmd(sock, "T,-1000, 500") # turns up the motor A
    wait(150)

    return sock

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

    send_cmd(sock, "T, 250, 480") # turns down the motor A
    wait(500)

    move_motors(-75, -75, degrees=30)  # twists to put the blocks in the black grid
    wait(250)
    move_motors(75, 75, degrees=50) # twists to put the blocks in the black grid

    move_motors(-300, 300, rotations=0.15)

    send_cmd(sock, "T,-1000, 500") # turns up the motor A
    wait(150)

    move_motors(-500, 500, rotations=1.52) # moves to go and get the second row
    wait(150)

    move_motors(500, 500, rotations=0.75) # moves to go and get the second row
    wait(150)

    move_motors(-500, 500, rotations=1.95) # moves to go and get the second row
    wait(150)

    while colorsensorLeft.reflection() > 30:   # moves to go and get the second row
        left_motor.run(-500)
        right_motor.run(500)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(250)

    move_motors(-300, 300, rotations=0.15)   # moves to go and get the second row
    wait(150)

    move_motors(-500, -500, rotations=0.75)   # moves to go and get the second row
    wait(150)

    pid_line_follower(follow_sensor_port=Port.S1,   # moves to go and get the second row
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="l")
    wait(250)

    move_motors(-500, 500, rotations=0.15)  # moves to go and get the second row
    wait(150)

    pid_line_follower(follow_sensor_port=Port.S1,   # moves to go and get the second row
                        stop_sensor_port=Port.S4,
                        base_speed=250,
                        Kp=2, Kd=3, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=22,
                        side="l")

    wait(250)

    move_motors(-250, 250, rotations=0.95) # moves to go and get the second row
    wait(250)

    move_motors(-250, -250, rotations=0.75) # moves to go and get the second row
    wait(250)

    move_motors(-250, 250, rotations=0.42) # moves to go and get the second row
    wait(250)

    motor_a.run_angle(600, 260) # moves down the 3d print with the second row
    wait(250)

    motor_d.run(500) # holds the blocks in place
    wait(150)

    motor_a.run_time(-1000, 900) # moves up the 3d print with the second row
    wait(250)

    move_motors(500, -500, rotations=0.55) # goes to take the first tool
    wait(150)

    move_motors(-500, -500, rotations=0.745)
    wait(150)

    move_motors(-500, 500, rotations=0.9)
    wait(150)


    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=400,
                        Kp=2, Kd=2, Ki=0,
                        target=47,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="r")
    
    wait(250)

    move_motors(-300, 300, rotations=0.45)
    wait(150)

    move_motors(500, 500, rotations=0.5)
    wait(150)

    send_cmd(sock,"T, 500, 450") # turns down the motor A
    wait(500)

    move_motors(-500, -500, rotations=0.5)
    wait(150)

    move_motors(500, -500, rotations=1.7)
    wait(150)

    move_motors(500, 500, rotations=0.745)
    wait(150)

    send_cmd(sock, "T, -750, 500") # turns up motor A
    wait(600)

    return sock