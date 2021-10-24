#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

def colorSwitcher(argument):
    notes = {
        Color.RED: 400,
        Color.BLUE: 450,
        Color.YELLOW: 500,
        Color.GREEN: 550
    }
    return notes.get(argument, -1)

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
#init Sensor
CSensor = ColorSensor(Port.S3)


# Write your program here.

while True:
    x = colorSwitcher( CSensor.color() )
    if x>0:
        ev3.speaker.beep(x,500)
        time.sleep(0.5)
    else:
        time.sleep(0.1)