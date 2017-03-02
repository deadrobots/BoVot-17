import motorsPlusPlus as x
import utils as u
import constants as c

from wallaby import *


def init():
    print "init"
    if c.isClone:
        print "i am clone"
    else:
        print "i am prime"
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armUpBotguy, 100)
    u.move_servo(c.outrigger, c.outriggerIn, 10)
    #u.move_servo(c.servoCow,c.cowMid,100)
    enable_servos()
    u.waitForButton()
    c.startTime = seconds()


def getBotGuy():
    print "getBotGuy"
    x.drive_speed(20, 50)
    x.rotate(-44, 25)
    #u.move_servo(c.outrigger, c.outriggerSafe, 10)
    if c.isClone:
        x.drive_speed(18, 100)
        x.rotate(95,50)
    else:
        x.drive_speed(34, 100)
        print "time to rotate"
        x.rotate(90, 50)
    u.move_servo(c.outrigger, c.outriggerSafe, 10)
    u.move_servo(c.servoArm, c.armBotguy, 10)
    msleep(300)
    x.drive_speed(30,100) #Check for moving over bump. Possible change for later.
    u.move_servo(c.servoArm, c.armDown-100, 10)
    msleep(200)
    u.move_servo(c.servoClaw, c.clawClose, 100)
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 10)
    if c.isClone:
        x.drive_speed(7,-20)
        u.move_servo(c.servoArm, c.armUpBotguy, 10)
        u.DEBUG()
    else:
        x.drive_speed(7, -20)
    u.move_servo(c.outrigger, c.outriggerIn, 10)
    msleep(300)
    u.move_servo(c.servoArm, c.armUpBotguy, 10)

def goToCow():
    print "goToCow"
    msleep(300)
    #u.move_servo(c.servoCow, c.cowUp, 10)
    msleep(300)
    x.drive_speed(5, -50)
    x.rotate(-90, 20)
    x.drive_speed(14, 50)
    x.rotate(187, 20)
    x.drive_speed(2, -50)
    u.move_servo(c.outrigger, c.outriggerOut, 10 )


def findCow():
    u.move_servo(c.servoArm, c.armUpLineFollow, 10)
    u.move_servo(c.servoCowClaw, c.cowClawOpen, 10)
    motor_power(c.COWMOTOR, -50)
    msleep(500)
    motor_power(c.COWMOTOR,-10)
    msleep(1000)
    time = seconds() + 2.0
    while (seconds() < time):
        if (analog(0) < 1000):
            x._drive(-30,-50)
        else:
            x._drive(-50,-30)
    x._drive(0,0)
    u.DEBUGwithWait()
def grabCowAndGo():
    print "grabCowAndGo"
    motor_power(c.COWMOTOR,10)
    msleep(2000)

    u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
    u.DEBUGwithWait()
    #u.waitForButton()
    #u.move_servo(c.servoCow, c.cowUp,10)
    msleep(300)
    x.drive_speed(34, 100)

def toOtherSide():
    print "toOtherSide"
    x.rotate(-79, 50)
    x.drive_speed(30, 50)
    x.drive_speed(-5, 50)
    x.rotate(-97, 50)
    u.move_servo(c.servoArm, c.armDown)
    x.drive_speed(15, 75)
    u.move_servo(c.servoArm, c.armBotguy)
    x.drive_speed(17,75)
    x.rotate(83,50)
    x.drive_speed(15,70)
    u.move_servo(c.servoArm, c.armUpBotguy)
    x.rotate(97 , 50)
    x.drive_speed(25,100)

    u.DEBUGwithWait()

def upRamp():
    print "upRamp"
    x.rotate(25, 50)
    x.drive_speed(36, 100)
    x.drive_speed(6, -50)
    x.rotate(89, 50)
    x.drive_speed(30, 100)
    x.drive_speed(4, -50)
    x.rotate(79, 50)
    u.move_servo(c.servoArm, c.armBotguy,10)
    msleep(300)
    x.drive_speed(70, 75)
    u.move_servo(c.servoCow, c.cowDown, 10)
    msleep(300)
    x.rotate(-45, 50)

def test():
    print "test"
    #u.move_servo(c.servoArm, c.armUp, 20)
    #x.drive_speed(50,55)
    x.rotate(90,50)


    print "Seconds elapsed: " + seconds() - c.startTime