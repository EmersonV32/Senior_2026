#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
from line_follower import pid_line_follower
from taking import mozaic
from outil1 import tool1, test1
from outil2 import tool2, test2
from ciment import aroundgrid, test3

ev3 = EV3Brick()

'''
#version 1 
mozaic()
sock=tool1()
tool2(sock)
aroundgrid(sock)
'''


#version 2
#mozaic()
sock=test1()
test2(sock)
test3(sock)