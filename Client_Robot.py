#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.messaging import BluetoothMailboxClient, NumericMailbox, TextMailbox
from pybricks.tools import wait

ev3 = EV3Brick()
motorA = Motor(Port.A)

client = BluetoothMailboxClient()
mbox = TextMailbox("cmd", client)

ev3.screen.print("Connecting...")
ev3.light.on(Color.ORANGE)
client.connect("ev3dev")
ev3.screen.print("Connected")
ev3.light.on(Color.GREEN)


while True:
    mbox.wait()
    msg = mbox.read()

    parts = msg.split(",")
    motor_name = parts[0]
    mode = parts[1]
    speed = int(parts[2])
    value = int(parts[3])

    if motor_name == "D":
        if mode == "T":
            motorD.run_time(speed, value)
        elif mode == "A":
            motorD.run_angle(speed, value)

    elif motor_name == "A":
        if mode == "T":
            motorA.run_time(speed, value)
        elif mode == "A":
            motorA.run_angle(speed, value)


'''
while True:
    mbox.wait()
    msg = mbox.read()

    motor_name, speed_str, time_str = msg.split(",")

    speed = int(speed_str)
    time_ms = int(time_str)

    if motor_name == "A":
        motorA.run_time(speed, time_ms)

    elif motor_name == "D":
        motorD.run_time(speed, time_ms)
'''



'''
mbox.wait()
time_ms = mbox.read()
motorA.run_time(1000, time_ms)

wait(1000)

mbox.wait()
time_ms = mbox.read()
motorA.run_time(-1000, time_ms)
'''













'''
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import (
    BluetoothMailboxServer,
    BluetoothMailboxClient,
    TextMailbox,
)
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait
import math

from pybricks.tools import StopWatch, wait
mA = Motor(Port.A)
ev3 = EV3Brick()
ev3.speaker.beep()


ROLE         = "client"        
PEER_NAME    = "ev3dev"         # Bluetooth name of the SERVER brick (EV3-B)
MAILBOX_NAME = "command"  
ev3.screen.clear()
screen = ev3.screen

def pairing():
    try:
        if ROLE.lower() == "server":
            run_server()
        else:
            run_client()
    finally :
        wait(100)

def run_server():
    global server, mbox
    ev3.screen.print("Server, Waiting for client)")
    ev3.light.on(Color.ORANGE)
    server = BluetoothMailboxServer()
    mbox   = TextMailbox(MAILBOX_NAME, server)
    server.wait_for_connection()
    ev3.screen.print("Server: connected")
    ev3.light.on(Color.GREEN)
    mbox.wait()
    ev3.screen.print(mbox.read())
    ev3.speaker.beep(880, 150)
    mbox.send("Server : Hello client")
    wait(3000)

    mbox.send("360")
    ev3.speaker.beep(880, 150)
    wait(1000)

def run_client():
    global client, mbox
    ev3.screen.print("Client connecting")
    ev3.light.on(Color.ORANGE)
    client = BluetoothMailboxClient()
    mbox   = TextMailbox(MAILBOX_NAME, client)
    for i in range(8):
        try:
            client.connect(PEER_NAME)        
            break
        except OSError as e:
            ev3.screen.print("Failed:", "retry", i+1, "/ 8")
            wait(1000)
    else:
        ev3.screen.print("CONNECT TimeOUT")
        return
    ev3.screen.print("Server connected")
    ev3.light.on(Color.GREEN)
    mbox.send("Client : Hello server")
    mbox.wait()
    ev3.screen.print(mbox.read())
    ev3.speaker.beep(880, 150)
    wait(3000)


    if mbox.read() == "3600":
        mA.run_angle(500, 360)      
        print("Motor A turned 360°")
    wait(1000)
    
pairing()
'''
