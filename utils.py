'''
Created on Jan 3, 2016
@author: graysonelias
'''

'''
This module provides some of our standard methods.
'''

import constants as c

from wallaby import ao
from wallaby import msleep
from wallaby import digital
from wallaby import seconds
from wallaby import freeze
from wallaby import set_servo_position
from wallaby import get_servo_position
from wallaby import analog
from wallaby import enable_servos
from motorsPlusPlus import rotate
from motorsPlusPlus import pivot_left
from motorsPlusPlus import drive_condition
from motorsPlusPlus import drive_speed

# Servo Constants
DELAY = 10
# Loop break timers #
time = 0  # This represents how long to wait before breaking a loop.

#Causes the robot to stop until the right button is pressed
def waitForButton():
    print "Press Button..."
    while not digital(c.RIGHT_BUTTON):
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)


#Causes the robot to stop
def DEBUG():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    exit(0)


#Causes the robot to stop and hold its position for 5 seconds
def DEBUGwithWait():
    DEBUG()
    msleep(5000)
    exit(0)


#Checks if there is a black line under the left tophat
def seeLineOne():
    return analog(0) < 2000


#Checks is there is a black line under the right tophat
def seeLineTwo():
    return analog(1) > 2000


#Checks to see if all of the servos, motors, and sensors are working properly
def start_up_test():
    set_servo_position(c.servoCowArm, c.cowArmDown)
    enable_servos()
    move_servo(c.servoCowArm, c.cowArmStart, 10)
    pivot_left(45, 25)
    msleep(500)
    pivot_left(-45, 25)
    msleep(500)
    move_servo(c.servoArm, c.armUp, 10)
    move_servo(c.servoClaw, c.clawOpen, 10)
    move_servo(c.servoCowClaw, c.cowClawOpen, 10)

    print "i need to see something"
    while analog(c.ET) < 1000:
        pass
    print "please, no more"
    while analog(c.ET) > 1000:
        pass
    print "show me again"
    while analog(c.ET) < 1000:
        pass

    msleep(500)
    drive_condition(50, 50, seeLineOne, True)
    msleep(500)
    drive_condition(-50, -50, seeLineTwo, True)



# Servo Control #

# Moves a servo with increment "speed".
def move_servo(servo, endPos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if speed == 0:
        speed = 2047
    if endPos >= 2048:
        print "Programmer Error"
        exit(0)
    if endPos < 0:
        print "Programmer Error"
        exit(0)
    if now > endPos:
        speed = -speed
    for i in range(int(now), int(endPos), int(speed)):
        set_servo_position(servo, i)
        msleep(DELAY)
    set_servo_position(servo, endPos)
    msleep(DELAY)


# Moves a servo with increment "speed".
def move_servo_on_white(servo, endPos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if speed == 0:
        speed = 2047
    if endPos >= 2048:
        print "Programmer Error"
        exit(0)
    if endPos < 0:
        print "Programmer Error"
        exit(0)
    if now > endPos:
        speed = -speed
    for i in range(int(now), int(endPos), int(speed)):
        set_servo_position(servo, i)
        msleep(DELAY)
        if seeBlackLeft():
            rotate(20, 25)
    set_servo_position(servo, endPos)
    msleep(DELAY)

#Gets the robot to the correct start position
def position():
    if c.isClone:
        drive_speed(-2, 25)
        drive_speed(2.15, 50)
        pivot_left(48, 25)
        drive_speed(.03, 25)
    else:
        #drive_speed(-1, 15)
        drive_speed(3.6, 50)
        rotate(-40, 25)     #use to be 49
        #drive_speed(.03, 25)


def seeBlackLeft():
    return analog(c.LTOPHAT) > 1500

def seeBlackRight():
    return analog(c.RTOPHAT) > 1500

def seeBlackRightTime():
    return analog(c.RTOPHAT) > 1500 and getWait()

# Moves a servo over a specific time.
def move_servo_timed(servo, endPos, time):
    if time == 0:
        speed = 2047
    else:
        speed = abs((DELAY * (get_servo_position(servo) - endPos)) / time)
    move_servo(servo, endPos, speed)


# Sets wait time in seconds before breaking a loop.
def setWait(DELAY):
    global time
    time = seconds() + DELAY

# Used to break a loop after using "setWait". An example would be: setWiat(10) | while true and getWait(): do something().
def getWait():
    return seconds() < time
