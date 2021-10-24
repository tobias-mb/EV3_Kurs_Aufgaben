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

def buttonSwitcher(argument):
    notes = {
        Button.UP: 400,
        Button.LEFT: 450,
        Button.DOWN: 500,
        Button.RIGHT: 550
    }
    return notes.get(argument, -1)

# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
while True:
    # should throw error whenever no button is pressed
    try:
        ev3.speaker.beep( buttonSwitcher( ev3.buttons.pressed()[0] ), 500 )
        time.sleep(0.1)
    except:
        time.sleep(0.1)