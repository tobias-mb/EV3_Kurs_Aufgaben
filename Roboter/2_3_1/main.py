#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
# init Motor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=130)

# Write your program here.
ev3.speaker.beep(442,500)
for x in range(4):
    robot.straight(300)
    robot.turn(90)
ev3.speaker.beep(442,500)