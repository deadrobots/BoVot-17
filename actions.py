import motorsPlusPlus as x
import utils as u
import constants as c
from wallaby import enable_servos, msleep, seconds



def init():
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    print "This is init"
    u.move_servo(c.servoArm, c.armDown, 100)
    u.move_servo(c.outrigger, c.outriggerIn, 10)
    #u.move_servo(c.servoCow,c.cowMid,100)
    enable_servos()
    u.waitForButton()
    c.startTime = seconds()

def getBotGuy():
    x.drive_speed(13.75, 50)
    x.rotate(-86, 50)
    u.move_servo(c.outrigger, c.outriggerSafe, 10)
    x.drive_speed(33, 100)
    x.rotate(85, 50)
    u.move_servo(c.servoArm, c.armBotguy, 10)
    x.drive_speed(30,100) #Check for moving over bump. Possible change for later.
    u.move_servo(c.servoArm, c.armDown, 10)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawClose, 10)
    msleep(500)
    u.move_servo(c.servoArm, c.armUp, 10)
    x.drive_speed(7, -20)
    u.move_servo(c.outrigger, c.outriggerIn, 10)
    msleep(300)
    u.move_servo(c.servoArm, c.armUpBotguy, 10)

def goToCow():
    msleep(300)
    #u.move_servo(c.servoCow, c.cowUp, 10)
    msleep(300)
    x.drive_speed(7, -50)
    x.rotate(-90, 20)
    x.drive_speed(14, 50)
    x.rotate(185, 20)
    x.drive_speed(2, 50)
    u.DEBUG()
    x.drive_speed(9, -50)

def grabCowAndGo():
    u.move_servo(c.servoCowClaw, c.cowClawOpen, 10)
    msleep(500)
    #u.move_servo(c.servoCow, c.cowDown, 10)
    msleep(1000)
    u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
    u.waitForButton()
    #u.move_servo(c.servoCow, c.cowUp,10)
    msleep(300)
    x.drive_speed(34, 100)

def toOtherSide():
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


    print "Seconds elapsed: " + seconds() - c.startTime