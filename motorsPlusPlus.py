'''
Created on Aug 7, 2016
@author: graysonelias
'''

'''
This module tries to provide more accurate motor commands.
It requires boolean "isClone", integer "LMOTOR", and integer "RMOTOR" from a "constants" module.
These values refer to prime/clone status, the left motor's port, and the right motor's port respectively.
'''

from constants import isClone
from constants import LMOTOR
from constants import RMOTOR
from constants import LTOPHAT


from math import pi

from wallaby import ao
from wallaby import clear_motor_position_counter
from wallaby import freeze
from wallaby import get_motor_position_counter
from wallaby import motor
from wallaby import msleep
from wallaby import seconds
from wallaby import analog
from wallaby import accel_x
from wallaby import motor_power

# Drive Constants
INCHES_TO_TICKS = 172#169   #205 - 161     #156#127#50 cm #265
WHEEL_DISTANCE = 4.25 #205 - 4.25  # Distance between the two wheels
ADJUST = 1.04 # adjust left wheel counter to fix drift (was 1.05)

from wallaby import digital

if isClone:
    # Drive Constants
    INCHES_TO_TICKS = 165  # 169   #205 - 161     #156#127#50 cm #265
    WHEEL_DISTANCE = 4.25  # 205 - 4.25  # Distance between the two wheels
    ADJUST = 0.963 #0.98  # adjust left wheel counter to fix drift


# Motor Control #

def _drive(left, right):  # Moves the robot using motor commands.
    motor(LMOTOR, left)
    motor(RMOTOR, right)



def _stop():  # Turns off all the motors.
    ao()


def drive_power(left, right):
    motor_power(LMOTOR, left)
    motor_power(RMOTOR, right)

def freeze_motors():  # Locks the motors to reduce drift.
    freeze(LMOTOR)
    freeze(RMOTOR)


def _right_ticks():  # Returns the right motor's tick count.
    return abs(get_motor_position_counter(RMOTOR))


def _left_ticks():  # Returns the left motor's tick count.
    return abs(get_motor_position_counter(LMOTOR) * ADJUST)


def _clear_ticks():  # Clears the motor ticks.
    clear_motor_position_counter(RMOTOR)
    clear_motor_position_counter(LMOTOR)


def calibrate(dist=0, num=0):  # WIP: Used to calibrate the constants for this module. Run as "calibrate()" to begin.
    if dist is 0:
        _clear_ticks()
        _drive(30, 30)
        msleep(3000)
        freeze_motors()
        print "Run the calibrate method again, but pass the distance traveled (inch) and the following number in:"
        print (_right_ticks() + _left_ticks()) / 2
    elif num is 0:
        drive_speed(6, 30)
        print "did it go " + str(dist) + " inches? If not, make slight adjustments to INCHES_TO_TICKS until it does."
    else:
        print "enter " + str(int(num / dist)) + " as INCHES_TO_TICKS. run calibrate again, but as calibrate(" + str(
            dist) + ", 0)"
    exit(0)


def arc_radius(angle, turnRadius, speed):  # Turns the robot "angle" degrees by arcing about "turnRadius".
    smallCircRadius = turnRadius - (WHEEL_DISTANCE / 2)
    largeCircRadius = turnRadius + (WHEEL_DISTANCE / 2)
    smallCircum = pi * 2 * smallCircRadius
    largeCircum = pi * 2 * largeCircRadius
    smallCircSeg = (angle / 360.0) * smallCircum
    largeCircSeg = (angle / 360.0) * largeCircum
    if turnRadius < 0:
        speed = -speed
    _clear_ticks()
    smallTicks = abs(INCHES_TO_TICKS * smallCircSeg)
    largeTicks = abs(INCHES_TO_TICKS * largeCircSeg)
    if angle > 0:
        smallSpeed = int(speed * (smallTicks / largeTicks))
        largeSpeed = int(speed)
        print smallTicks
        print largeTicks
        print smallTicks / largeTicks
        print smallSpeed
        print largeSpeed
        while _right_ticks() <= largeTicks:
            if (_right_ticks() / largeTicks) == (_left_ticks() / smallTicks):
                _drive(smallSpeed, largeSpeed)
            if (_right_ticks() / largeTicks) > (_left_ticks() / smallTicks):
                _drive(smallSpeed, int(largeSpeed / 1.3))
            if (_left_ticks() / smallTicks) > (_right_ticks() / largeTicks):
                _drive(int(smallSpeed / 1.3), largeSpeed)
    else:
        smallSpeed = int(speed * (smallTicks / largeTicks))
        largeSpeed = int(speed)
        print smallTicks
        print largeTicks
        print smallTicks / largeTicks
        print smallSpeed
        print largeSpeed
        while _left_ticks() <= largeTicks:
            if (_left_ticks() / largeTicks) == (_right_ticks() / smallTicks):
                _drive(largeSpeed, smallSpeed)
            if (_left_ticks() / largeTicks) > (_right_ticks() / smallTicks):
                _drive(largeSpeed, int(smallSpeed / 1.3))
            if (_right_ticks() / smallTicks) > (_left_ticks() / largeTicks):
                _drive(int(largeSpeed / 1.3), smallSpeed)
    freeze_motors()
    print smallTicks
    print largeTicks
    print get_motor_position_counter(RMOTOR)



def drive_speed(inches, speed):  # Drives an exact distance in inches.
    print "driving exact distance"
    if inches < 0:
        speed = -speed
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * inches)
    while _right_ticks() <= ticks:
        if _right_ticks() == _left_ticks():
            _drive(speed, speed)
        if _right_ticks() > _left_ticks():
            _drive(speed, int(speed / 1.3))
        if _left_ticks() > _right_ticks():
            _drive(int(speed / 1.3), speed)
    freeze_motors()
    print ticks
    print get_motor_position_counter(RMOTOR)


def drive_timed(lmotor, rmotor, time):
    print "driving timed"
    _clear_ticks()
    end = seconds() + time
    if lmotor == 0 or rmotor == 0:
        print "please use pivot instead!"

    elif abs(rmotor) <= abs(lmotor):
        mod = rmotor / (lmotor * 1.0)
        newLeftSpeed = lmotor
        newRightSpeed = int(mod * lmotor)
    elif abs(lmotor) < abs(rmotor):
        mod = (lmotor * 1.0) / rmotor
        newLeftSpeed = int(mod * rmotor)
        newRightSpeed = rmotor
    while seconds() <= end:
        if int(_right_ticks() / mod) == int(_left_ticks() / mod):
            _drive(newLeftSpeed, newRightSpeed)
        if int(_right_ticks() / mod) > int(_left_ticks() / mod):
            _drive(newLeftSpeed, int(newRightSpeed / 1.3))
        if int(_left_ticks() / mod) > int(_right_ticks() / mod):
            _drive(int(newLeftSpeed / 1.3), newRightSpeed)
    freeze_motors()
print get_motor_position_counter(RMOTOR)


def drive_condition(lmotor, rmotor, testFunction,
                    state=True):  # Drives while "testFunction" returns "state" | an example would be: x.drive_condition(50, 50, x.getWait)
    print "driving under condition"
    _clear_ticks()
    if lmotor == 0 or rmotor == 0:
        print "this won't work! please use pivot_right_condition or pivot_left_condition instead!"
        exit(0)

    elif abs(rmotor) <= abs(lmotor):
        mod = rmotor / (lmotor * 1.0)
        newLeftSpeed = lmotor
        newRightSpeed = int(mod * lmotor)
    elif abs(lmotor) < abs(rmotor):
        mod = (lmotor * 1.0) / rmotor
        newLeftSpeed = int(mod * rmotor)
        newRightSpeed = rmotor
    while testFunction() is state:
        if int(_right_ticks() / mod) == int(_left_ticks() / mod):
            _drive(newLeftSpeed, newRightSpeed)
        if int(_right_ticks() / mod) > int(_left_ticks() / mod):
            _drive(newLeftSpeed, int(newRightSpeed / 1.3))
        if int(_left_ticks() / mod) > int(_right_ticks() / mod):
            _drive(int(newLeftSpeed / 1.3), newRightSpeed)
    freeze_motors()
    print get_motor_position_counter(RMOTOR)


def rotate(deg, speed):  # Rotates by using both wheels equally.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE
    inches = angle * circ
    print circ
    print inches
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(-speed, speed)
    while _right_ticks() <= ticks:
        pass
    freeze_motors()
    print get_motor_position_counter(RMOTOR)


def pivot_right(deg, speed):  # Pivots by moving the right wheel.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE * 2
    inches = angle * circ
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(0, speed)
    while _right_ticks() <= ticks:
        pass
    freeze_motors()

def pivot_right_condition(speed, testFunction, state=True):  # Pivots by moving the right wheel.
    _drive(0, speed)
    while testFunction() is state:
        pass
    freeze_motors()

def pivot_left(deg, speed):  # Pivots by moving the left wheel.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE * 2
    inches = angle * circ
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(speed, 0)
    while _left_ticks() <= ticks:
        pass
    freeze_motors()

def pivot_left_condition(speed, testFunction, state=True):  # Pivots by moving the left wheel.
    _drive(speed, 0)
    while testFunction() is state:
        pass
    freeze_motors()

def line_follow(distance):
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * distance)
    while _right_ticks() <= ticks:
        if analog(0) >1500:
            _drive(-40, -30)
        else:
            _drive(-30, -40)
    _drive(0,0)


def line_follow_forward(distance):
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * distance)
    while _right_ticks() <= ticks:
        if analog(0) >1500:
            _drive(30, 40)
        else:
            _drive(40, 30)
    _drive(0,0)

def line_follow_forward_end(port):
    i = 0
    while (i < 21):
        print i
        if analog(port) > 1500:
            i = 0
            drive_timed(30, 80, .02)
        else:
            i = i + 1
            drive_timed(80, 30, .02)

def line_follow_ramp (distance):
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * distance)
    i = 0
    maxSpeed = 60
    count = 0
    while count < 3:
        #if analog(0) <1500 and analog(1) <1500
        #else:
        if accel_x() < 0:
            count = 0
        else:
            count += 1
        if i == 50:
            maxSpeed = 40
        if analog(LTOPHAT) > 2300:
            _drive(30, maxSpeed)
            print ("On black Turn Left")
        elif analog(LTOPHAT) < 1700:
            _drive(maxSpeed, 30)
            print("On white Turn Right")
        else:
            _drive(45,45)
            print("Going straight")
            i = i + 1
            print(i)
        msleep(20)
    _drive(0, 0)
    #freeze_motors()

def line_follow_terrace (distance):
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * distance)
    while _right_ticks() <= ticks:
        #if analog(0) <1500 and analog(1) <1500
        #else:
        if analog(LTOPHAT) > 2300:
            _drive(30, 35)
            print ("On black turn left")
        elif analog(LTOPHAT)<1700:
            _drive(35, 30)
            print("On White turn right")
        else:
            _drive(30,30)
            print ("going straight")

        msleep(10)
    freeze_motors()

def change_adjust(x):
    global ADJUST
    if x:
        print("Adjusted to new value")
        ADJUST = .9685
    else:
        print("Resetting to old value")
        if isClone:
            ADJUST = 0.98
        else:
            ADJUST = 1.08
        ADJUST = 1.08 # add if clone 0.98

def calibrate3():
    AMOUNT = 6000
    _clear_ticks()
    _drive(50, 50)
    startR = seconds()
    while _right_ticks() < AMOUNT:
        pass
    endR = seconds() - startR
    freeze_motors()
    msleep(5000)
    _clear_ticks()
    _drive(50, 50)
    startL = seconds()
    while _left_ticks() < AMOUNT:
        pass
    endL = seconds() - startL

    print "Value: " + str(endL / endR)


    #1.07
    # 0.93
from constants import ET


def find_pole():
    value = analog(ET)
    highest_value = value
    _drive(50, 52)
    print "new highest: " + str(value)
    for _ in range(0, 3):
        while value > 0.5 * highest_value or highest_value < 1000:
            if value > highest_value:
                highest_value = value
                print "new highest: " + str(value)
            msleep(10)
            value = analog(ET)
            # print value
        print "exited on: " + str(value)
        value = analog(ET)
    freeze_motors()

from utils import seeBlackLeft, seeBlackRight

def drive_speed_saw_black(inches, speed):  # Drives an exact distance in inches.
    print "driving exact distance"
    sawBlack = False
    if inches < 0:
        speed = -speed
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * inches)
    while _right_ticks() <= ticks:
        if _right_ticks() == _left_ticks():
            _drive(speed, speed)
        if _right_ticks() > _left_ticks():
            _drive(speed, int(speed / 1.3))
        if _left_ticks() > _right_ticks():
            _drive(int(speed / 1.3), speed)
        if seeBlackRight() or seeBlackLeft():
            sawBlack = True
    freeze_motors()
    print ticks
    print get_motor_position_counter(RMOTOR)
    if seeBlackRight() or seeBlackLeft():
        return 0
    elif sawBlack:
        return 1
    else:
        return 2