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
#init Sensor
UltraSensor = UltrasonicSensor(Port.S4)
TSensor = TouchSensor(Port.S1)
CSensor = ColorSensor(Port.S3)

# Write your program here.
robot.drive(120,0)
counter = 0
ev3.screen.clear()
ev3.screen.print('\n\t', counter)
while True:
    if CSensor.color() == Color.BLACK:
        counter +=1
        ev3.speaker.beep()
        ev3.screen.clear()
        ev3.screen.print('\n\t', counter)
        # wait until no longer black
        col_cond = False
        while not col_cond:
            if not (CSensor.color() == Color.BLACK):
                col_cond = True
                break
            else:
                time.sleep(0.1)
        
    else:
        time.sleep(0.1)
