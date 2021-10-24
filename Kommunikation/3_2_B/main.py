#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from umqtt.robust import MQTTClient
import time

#MQTT setup
MQTT_ClientID = 'RobotB'
MQTT_Broker = '192.168.0.213'
MQTT_Topic_Hallo = 'Lego/Hallo'
client = MQTTClient(MQTT_ClientID, MQTT_Broker)


#callback for listen to topics
received_message = False
def listen(topic,msg):
    global received_message
    if str(msg.decode()) == 'move!':
        received_message = True


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
client.connect()
time.sleep(0.5)
client.set_callback(listen)
client.subscribe(MQTT_Topic_Hallo)
ev3.speaker.beep()
ev3.screen.print('listening')

# wait until message
while not received_message:
    client.check_msg()
    time.sleep(0.5)

robot.straight(500)
time.sleep(10)