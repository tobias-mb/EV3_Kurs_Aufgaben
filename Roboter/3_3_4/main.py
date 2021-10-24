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
speed = 80
turn_rate = 40
while not(CSensor.color() == Color.RED):
    sensor_value = CSensor.color()
    if sensor_value == Color.BLACK or sensor_value == Color.WHITE:
        if sensor_value == Color.BLACK:
            speed = 80
            turn_rate = 40
        if sensor_value == Color.WHITE:
            speed = 40
            turn_rate = 20
        robot.drive(speed,turn_rate)
    else:
        robot.drive(speed,-turn_rate)

robot.stop()
ev3.speaker.beep(442,500)
