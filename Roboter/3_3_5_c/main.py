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

def printCounter(counter):
    ev3.screen.print('blue: ', counter[Color.BLUE])
    ev3.screen.print('red: ', counter[Color.RED])
    ev3.screen.print('green: ', counter[Color.GREEN])
    ev3.screen.print('yellow: ', counter[Color.YELLOW])

def colorSwitcher(argument):
    notes = {
        Color.RED: 'C4/4',
        Color.BLUE: 'E4/4',
        Color.YELLOW: 'G4/4',
        Color.GREEN: 'C5/4'
    }
    return notes.get(argument, -1)

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
counter = {
    Color.BLUE : 0,
    Color.RED: 0,
    Color.GREEN: 0,
    Color.YELLOW: 0
}
color_order = []

#robot.drive(120,0)
ev3.screen.clear()
printCounter(counter)
tCond = False
while not tCond:
    col = CSensor.color()
    if (col == Color.BLUE or col == Color.RED or col == Color.GREEN or col == Color.YELLOW):
        color_order.append( colorSwitcher(col) )
        counter[col] +=1
        #ev3.speaker.beep()
        ev3.screen.clear()
        printCounter(counter)
        # wait until no longer color
        col_cond = False
        while not col_cond:
            col = CSensor.color()
            if not (col == Color.BLUE or col == Color.RED or col == Color.GREEN or col == Color.YELLOW):
                col_cond = True
                break
            else:
                time.sleep(0.1)
        
    else:
        if TSensor.pressed():
            tCond = True
        time.sleep(0.1)

ev3.speaker.play_notes(color_order, tempo=120)