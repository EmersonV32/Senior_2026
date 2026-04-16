#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import usocket as socket

ev3 = EV3Brick()
sock = socket.socket()
sock.connect(socket.getaddrinfo('192.168.0.1', 12345)[0][-1])

def send_cmd(cmd):
    sock.send((cmd + "\n").encode())

def done():
    send_cmd("done")
    sock.close()

def tools():
    # your tools section code goes here
    pass