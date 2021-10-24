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

# init Sensors
TSensor = TouchSensor(Port.S1)


# Write your program here.
ev3.speaker.beep(442,500)
counter = 0
t_end = time.time() + 5
ev3.screen.print('\n',counter)
while time.time() < t_end:
    if TSensor.pressed():
        # wait until TSensor is NOT pressed (anymore)
        while True:
            if not TSensor.pressed():
                break
            else:
                time.sleep(0.1)
        counter += 1
        ev3.screen.clear()
        ev3.screen.print('\n',counter)

for x in range(counter):
    ev3.speaker.beep(500,250)
    time.sleep(0.5)

