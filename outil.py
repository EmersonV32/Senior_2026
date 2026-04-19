#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
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

def tool():
    ev3.speaker.beep() 
    wait(500)
    ev3.speaker.beep()
    sock = socket.socket()

    connected = False
    while not connected:
        try:
            ev3.screen.print("Linking to Slave...")
            sock.connect(socket.getaddrinfo('192.168.2.1', 12345)[0][-1])
            connected = True
        except OSError:
            ev3.screen.print("Retry in 1s...")
            wait(1000) 

    ev3.screen.print("Connected!")
    ev3.speaker.beep()


    #sock.connect(socket.getaddrinfo('192.168.0.1', 12345)[0][-1])
    #ev3.speaker.beep() 


    move_motors(500, -500, rotations= 2.05)

    move_motors(-500, -500, rotations= 0.7)

    while colorsensorRight.reflection() > 18:
        left_motor.run(-500)
        right_motor.run(500)

    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    wait(100)

    move_motors(-500, 500, rotations=0.3)

    move_motors(500, 500, rotations= 0.7)

    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=350,
                        Kp=2.5, Kd=3, Ki=0,
                        target=50,
                        max_angle=850,
                        stop_mode="a",
                        stop_threshold=20,
                        side="r")


    pid_line_follower(follow_sensor_port=Port.S1,
                        stop_sensor_port=Port.S4,
                        base_speed=350,
                        Kp=2.5, Kd=3, Ki=0,
                        target=50,
                        max_angle=None,
                        stop_mode="c",
                        stop_threshold=20,
                        side="r")

    move_motors(500, 500, rotations=0.8)

    send_cmd(sock, "T,670,250")

    wait(500)

    move_motors(-500, -500, rotations=0.8)

    pid_line_follower(follow_sensor_port=Port.S1,
                    stop_sensor_port=Port.S4,
                    base_speed=467,
                    Kp=2.5, Kd=3, Ki=0,
                    target=50,
                    max_angle=1000,
                    stop_mode="a",
                    stop_threshold=20,
                    side="r")

    move_motors(-500, -500, rotations=0.8)

    send_cmd(sock, "T,-1000,300")

    wait(500)

    move_motors(-500, -500, rotations=0.7)




    done(sock)