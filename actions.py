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
    u.move_servo(c.servoCowClaw,c.cowClawStart,100)
    u.move_servo(c.cowArm, c.cowArmStart, 100)
    enable_servos()
    u.waitForButton()
    c.startTime = seconds()


def getBotGuy():
    print "getBotGuy"
    if c.isClone:
        x.drive_speed(20, 50)
        x.rotate(-44, 25)
    else:
        x.drive_speed(22, 50)
        x.rotate(-38, 25)
    x.drive_speed(16.5, 80)
    if c.isClone:
        x.rotate(85,50)
    else:
        x.rotate(91, 50)


    # u.move_servo(c.servoArm, c.armBotguy, 10)
    msleep(300)
    x.drive_speed(20,100) #Check for moving over bump. Possible change for later.
    x.drive_speed(4, -60)
    u.move_servo(c.servoArm, c.armDown, 10)
    x.drive_speed(5, 50)
    msleep(200)
    u.move_servo(c.servoClaw, c.clawClose, 100) # grab botguy
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 10)
    x.drive_speed(9.5,-20)
    u.move_servo(c.servoArm, c.armUpBotguy, 10)
    msleep(300)

def goToCow():
    print "goToCow"
    x.pivot_right(-93, 30)
    x.drive_speed(12, 40)
    if c.isClone:
        x.rotate(182, 30)
    else:
        x.rotate(181,30)

    print("new code here")
    motor_power(c.COWMOTOR, -50)
    msleep(500)
    motor_power(c.COWMOTOR, -10)
    msleep(1000)
    x.drive_speed(9, -50)
    u.DEBUGwithWait()



    # x.rotate(-90, 20)
    # x.drive_speed(5, -80)
    # x.rotate(182, 25)
    # u.DEBUGwithWait()
    # x.drive_speed(14, 50)
    # x.rotate(187, 20)
    # x.drive_speed(2, -50)

def findCow():
    print "findCow"
    u.move_servo(c.servoArm, c.armUpLineFollow, 10)
    x.drive_speed(12, -80)
    u.move_servo(c.servoCowClaw, c.cowClawOpen, 10)
    u.move_servo_on_white(c.outrigger, c.outriggerOut, 5) ###########################
    print"rotate twoward black"
    x.pivot_left_condition(25, u.onBlackFront, False) #######################
    motor_power(c.COWMOTOR, -50)
    msleep(500)
    motor_power(c.COWMOTOR, -10)
    msleep(1000)
    x.line_follow(25)



    ''''
    time = seconds() + 2.0
    while (seconds() < time):
        if (analog(0) < 1000):
            x._drive(-30,-50)
        else:
            x._drive(-50,-30)
    x._drive(0,0)
'''

def grabCowAndGo():
    print "grabCowAndGo"
    x.rotate(3, 20)
    msleep(1000)
    x.drive_speed(-7, 20)
    msleep(1000)
    x.rotate(-6, 10)
    u.move_servo(c.servoCowClaw, c.cowClawClose, 10)

    x.rotate(3, 10)

    ##### #####
    #Time Test#

    try:
        data = open("data.txt", "r").read()
    except Exception:
        data = ""
    open("data.txt", "w").write(data + "\n" + str(seconds() - c.startTime))

    print("\n\nDATA\n")
    print(open("data.txt", "r").read() + "\n\n")

    ###########

    motor_power(c.COWMOTOR, 40)
    msleep(2000)

def toOtherSide():
    print "toOtherSide"

    x.drive_speed(35.5, 50)
    x.rotate(-90, 30)
    x.drive_speed(28, 50)
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
    u.DEBUGwithWait()




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
    x.drive_speed(50,55)
    #x.rotate(90,50)


    print "Seconds elapsed: " + seconds() - c.startTime