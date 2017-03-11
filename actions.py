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
    u.waitForButton()
    c.startTime = seconds()
    #x.drive_speed(80, 100)
    # x.calibrate3()


def getBotGuy():
    print "getBotGuy"
    #Get out of start box
    if c.isClone:
        x.drive_speed(20, 50)
        x.rotate(-42, 25)
        x.drive_speed(16.5, 80)
        x.rotate(87, 50)
    else:
        # x.drive_speed(20, 100) #speed was 50
        # x.rotate(-41, 50) #speed was 25
        # x.drive_speed(17, 100) #speed was 80
        # x.rotate(89, 50)

        x.drive_speed(15, 100) #speed was 50
        msleep(200)
        x.rotate(-6, 50) #speed was 25
        msleep(200)
        x.drive_speed(25, 100)#speed was 80
        x.rotate(57, 50)


    msleep(300)
    x.drive_speed(6,100)#Check for moving over bump. Possible change for later.
    if c.isClone:
        x.drive_speed(4, -60)

    else:
        x.drive_speed(6, -60)
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armDown, 20)
    if c.isClone:
        x.drive_speed(5, 50)

    else:
        x.drive_speed(7, 50)
    msleep(200)
    u.move_servo(c.servoClaw, c.clawClose, 100) # grab botguy
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 10)

    if c.isClone:
        x.drive_speed(10.5,-20)
        u.move_servo(c.servoArm, c.armUpBotguy, 10)

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
        x.drive_speed(9, -50)
    else:
        x.rotate(175, 75) #was 30
        u.move_servo(c.cowArm, c.cowDown, 20)
        u.move_servo(c.servoCowClaw, c.cowClawOpen, 20)
        x.drive_speed(6, -80) #was -50
    print("new code here")
    u.DEBUGwithWait()


def findCow():
    camera_open()
    while True:
        camera_update()
        if get_object_count(0) > 0 and get_object_area(0, 0) > 1000:
            if get_object_center_x(0, 0) > 130:
                print "right"
                x.drive_timed(-70, 70, .01)
            elif get_object_center_x(0, 0) < 110:
                print "left"
                x.drive_timed(70, -70, .01)
            else:
                print "found it"
                break
        else:
            print "i see nothing"
            x.drive_timed(-70, 70, .01)
        #msleep(100)
    camera_close()


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


def grabCowAndGo():
    print "grabCowAndGo"
    if c.isClone:
        x.rotate(3, 20)
        msleep(1000)
        x.drive_speed(-7, 20)
        msleep(1000)
        x.rotate(-6, 10)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
        u.move_servo(c.cowArm, c.cowArmStart, 10)
        x.rotate(3, 10)
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

    x.drive_speed(30, 50)
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
    x.drive_speed(-20, 100)  #square up
    msleep(300)
    x.ADJUST = 1.07 #straighter drive, didn't want to mess up earlier values
    x.drive_speed(55, 100)
    msleep(300)
    u.DEBUGwithWait()
    x.rotate(15, 50)
    msleep(300)
    x.drive_speed(38, 100)
    x.drive_speed(6, -50)
    x.rotate(90, 50)
    x.drive_speed(30, 100)
    x.drive_speed(4, -50)
    x.rotate(82, 50)
    u.move_servo(c.servoArm, c.armUpRampBotGuy,10)
    u.DEBUGwithWait()
    msleep(300)
    x.drive_speed(70, 75)
    u.move_servo(c.cowArm, c.cowDown, 10)
    msleep(300)
    x.rotate(-45, 50)

def test():
    print "test"
    #u.move_servo(c.servoArm, c.armUp, 20)
    x.drive_speed(50,55)
    #x.rotate(90,50)


    print "Seconds elapsed: " + seconds() - c.startTime