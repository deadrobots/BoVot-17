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
    u.move_servo(c.servoClaw, c.clawClose, 100)
    u.move_servo(c.servoArm, c.armUpBotguy, 100)
    u.move_servo(c.servoCowClaw,c.cowClawStart,100)
    u.move_servo(c.cowArm, c.cowArmStart, 100)
    enable_servos()
    position()
    u.waitForButton()
    c.startTime = seconds()
    camera_open()
    #x.drive_speed(80, 100)
    #exit(0)
    # x.calibrate3()

def position():
    x.drive_speed(-2, 25)
    x.drive_speed(2.15, 50)
    x.pivot_left(48, 25)
    x.drive_speed(.03, 25)

def getBotGuy():
    print "getBotGuy"
    #Get out of start box

    x.drive_speed(15, 100)
    msleep(200)
    if c.isClone:
        x.rotate(-9, 50) #speed was 25
    else:
        x.rotate(-8,50)

    msleep(200)
    if c.isClone:
        x.drive_speed(23, 100)#speed was 80
    else:
        x.drive_speed(24,100)

    x.rotate(57, 50)

    msleep(300)
    x.drive_speed(6,100)#Check for moving over bump. Possible change for later.
    x.drive_timed(20, 100, 1/4)
    msleep(5000)
    x.drive_speed(6, -60)
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armDown, 20)
    x.drive_speed(7, 50)
    msleep(200)
    u.move_servo(c.servoClaw, c.clawClose, 100) # grab botguy
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 10)

    if c.isClone:
        x.drive_speed(5,-40)
        u.move_servo(c.servoArm, c.armUpBotguy, 10)
        x.drive_speed(4.5,-60)
    else:
        x.drive_speed(5, -40)
        u.move_servo(c.servoArm, c.armUpBotguy, 10)
        x.drive_speed(5.5, -60)
    msleep(300)

def goToCow():
    print "goToCow"
    x.pivot_right(-93, 75) #was 30
    x.drive_speed(12, 80) #was 40
    if c.isClone:
        x.rotate(182,30)
        u.move_servo(c.cowArm, c.cowDown, 20)
        u.move_servo(c.servoCowClaw, c.cowClawOpen, 20)
        x.drive_speed(6, -78)
    else:
        x.rotate(175, 50) #was 30 and then was 75
        u.move_servo(c.cowArm, c.cowDown, 20)
        u.move_servo(c.servoCowClaw, c.cowClawOpen, 20)
        x.drive_speed(6, -80) #was -50
    print("new code here")

def findCow():
    count = 0
    tries = 100
    while tries > 0:
        camera_update()
        if get_object_count(0) > 0 and get_object_area(0, 0) > 1000:
            print("i see something")
            if get_object_center_x(0, 0) > 130:
                print "right"
                count -= 1
                x.drive_timed(-30, 30, .01)
            elif get_object_center_x(0, 0) < 110:
                print "left"
                count += 1
                x.drive_timed(30, -30, .01)
            else:
                print "found it in " + str(100 - tries) + " tries"
                print(get_object_center_x(0, 0))
                print(get_object_area(0, 0))
                break
        else:
            print "i see nothing"
            tries -= 1
            msleep(10)
        #msleep(100)

    # while count != 0:
    #     if count > 0:
    #         count -= 1
    #         x.drive_timed(-70, 70, .01)
    #     else:
    #         count += 1
    #         x.drive_timed(70, -70, .01)

def grabCowAndGo():
    print "grabCowAndGo"
    if c.isClone:
        x.drive_speed(-5, 20)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
        u.move_servo(c.cowArm, c.cowArmStart, 10)
    else:
        #x.rotate(-2, 10)
        msleep(200)
        x.drive_speed(-10, 80) #was 20
        msleep(200)
        x.rotate(2, 10)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 80)
        u.move_servo(c.cowArm, c.cowArmStart, 20)
        #x.rotate(30, 10)


def toOtherSide():
    print "toOtherSide"
    if c.isClone:
        x.drive_speed(33, 85)
    else:
        x.drive_speed(39, 85)

    x.rotate(-84, 30)
    x.drive_speed(34, 80)
    u.DEBUGwithWait()
    x.drive_speed(-4, 30)
    x.pivot_right(45, 30)
    u.move_servo(c.servoArm, c.armBotguy, 10)
    x.drive_timed(-50, -20, 2)
    x.drive_speed(-17.5, 45)
    x.drive_timed(-50, -20, 2)
    x.pivot_right(43, 50)
    u.move_servo(c.servoArm, c.armUpBotguy, 15)
    x.drive_speed(5, 25)
    x.drive_speed(-24, 50)

def driveToCow2():
    x.rotate(90, 25)
    u.waitForButton()
    x.drive_speed(-26, 60)
    motor_power(c.COWMOTOR, -50)
    msleep(500)
    motor_power(c.COWMOTOR, -10)
    msleep(1000)
    u.move_servo(c.servoCowClaw, c.cowClawOpen, 10)
    x.drive_speed(-5, 50)
    msleep(500)
    motor_power(c.COWMOTOR, 40)

def pickUpCow2():
    x.drive_timed(-20, -25, 2)


    # x.drive_speed(4,-50)
    # x.change_adjust(True)
    # print("check me: " + str(x.ADJUST))
    # u.waitForButton()
    # x.drive_speed(52, 80)
    # x.rotate(90,25)
    # x.change_adjust(False)
    # u.DEBUGwithWait()
    # x.drive_speed(-5, 50)
    # x.rotate(-97, 50)
    # u.move_servo(c.servoArm, c.armDown)
    # x.drive_speed(15, 75)
    # u.move_servo(c.servoArm, c.armBotguy)
    # x.drive_speed(17,75)
    # x.rotate(83,50)
    # x.drive_speed(15,70)
    # u.move_servo(c.servoArm, c.armUpBotguy)
    # x.rotate(97 , 50)
    # x.drive_speed(25,100)


def seeWhite():
    return analog(0) < 1500


def upRamp():
    print "upRamp"
    # x.drive_speed(-20, 100)  #square up
    # msleep(300)
    # x.ADJUST = 1.07
    # x.drive_speed(20, 100)
    x.ADJUST = 1.07 #straighter drive, didn't want to mess up earlier values

    # x.drive_speed(35, 100)
    # x.drive_speed(38, 100)

    x.drive_condition(100, 100, seeWhite)
    x.pivot_right(45, 50)
    x.drive_speed(5, 50)
    x.pivot_right(45, 50)
    x.drive_speed(17, 80)
    x.drive_speed(-3, 50)
    x.pivot_left(-90, 85)
    x.drive_speed(-6, 50)

    # x.drive_speed(6, -50)
    # x.rotate(90, 50)
    # x.drive_speed(30, 100)
    # x.drive_speed(4, -50)
    # x.rotate(82, 50)
    u.move_servo(c.servoArm, c.armUpRampBotGuy,10)
    msleep(300)
    x.ADJUST = 1.04
    x.drive_speed(70, 75)
    u.move_servo(c.cowArm, c.cowArmTurn, 10)
    msleep(300)
    x.rotate(10, 25)
    msleep(100)
    u.move_servo(c.servoCowClaw, c.cowClawOpen)
    msleep(100)
    u.move_servo(c.cowArm, c.cowArmStart)
    msleep(100)
    u.move_servo(c.servoArm, c.botguyHover)
    msleep(100)
    x.rotate(-30, 25)
    u.move_servo(c.servoArm, c.armDown)
    print "did it work?"
    u.DEBUGwithWait()


def test():
    print "test"
    #u.move_servo(c.servoArm, c.armUp, 20)
    x.drive_speed(50,55)
    #x.rotate(90,50)


    print "Seconds elapsed: " + seconds() - c.startTime