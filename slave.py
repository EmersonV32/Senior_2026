#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import usocket as socket

ev3 = EV3Brick()

def send_cmd(sock, cmd):
    sock.send((cmd + "\n").encode())

def done(sock):
    send_cmd(sock, "done")
    sock.close()

sock = socket.socket()
sock.connect(socket.getaddrinfo('192.168.0.1', 12345)[0][-1])

send_cmd(sock, "A,500,360")
wait(1000)

done(sock)
