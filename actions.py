import motorsPlusPlus as x
import utils as u
import constants as c

from wallaby import *


# Tests all of the actuators and sensors
def init():
    print "init"
    if c.isClone:
        print "i am clone"
    else:
        print "i am prime"
    enable_servos()
    # u.start_up_test()
    u.waitForButton()
    u.move_servo(c.servoClaw, c.clawClose, 100)
    u.move_servo(c.servoArm, c.armUpBotguy, 100)
    u.move_servo(c.servoCowClaw, c.cowClawStart, 100)
    u.move_servo(c.servoCowArm, c.cowArmStart, 100)
    u.position()
    u.waitForButton()
    c.startTime = seconds()
    camera_open()


# Drives out of the start box and gets Botguy from the aquifer
def getBotGuy():
    print "getBotGuy"
    # Get out of start box

    x.arc_radius(5,90,100)
    x.drive_speed(23,100)
    msleep(100)
    x.rotate(-40,50)     #use to -45
    msleep(100)
    x.find_pole()
    x.drive_speed(1.5, 40)
    x.pivot_right(90, 30)
    x.drive_speed(5, 40)

    x.drive_speed(6, -60)
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armDown, 20)
    x.drive_speed(9, 50)
    msleep(200)
    u.move_servo(c.servoClaw, c.clawClose, 100)  # grab botguy
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 10)
    if c.isClone:
        x.drive_speed(5, -40)
        u.move_servo(c.servoArm, c.armUpBotguy, 10)
        x.drive_speed(4.5, -60)
    else:
        x.drive_speed(6, -40)
        u.move_servo(c.servoArm, c.armUpBotguy, 10)
        x.drive_speed(4.5, -60)
    msleep(300)


# Turns from the aquifer and goes toward the cow
def goToCow():
    print "goToCow"
    if c.isClone:
        x.pivot_right(-93, 75)  # was 30
        x.drive_speed(12, 80)  # was 40
        x.rotate(182, 30)
        u.move_servo(c.servoCowArm, c.cowArmDown, 20)
        u.move_servo(c.servoCowClaw, c.cowClawOpen, 20)
        x.drive_speed(6, -78)
    else:
        x.pivot_right(-81, 75)  # was 30
        x.drive_speed(12, 80)  # was 40
        x.rotate(172, 25)  # was 165
        u.move_servo(c.servoCowArm, c.cowArmDown, 20)
        u.move_servo(c.servoCowClaw, c.cowClawOpen, 20)
        x.drive_speed(8, -80)  # was -50

count = 0

# Uses the camera to locate the blue cow
def findCow():
    turns = 3
    for _ in range(0, turns):
        if center_on_cow():
            break
        x.rotate(10, 30)

def center_on_cow():
    camera_open()
    global count
    tries = 30
    while tries > 0:
        camera_update()
        if get_object_count(0) > 0 and get_object_area(0, 0) > 500:
            print("i see something")
            if get_object_center_x(0, 0) > 110:
                print "right"
                count -= 1
                x.drive_timed(-30, 30, .01)
                u.setWait(.3)
                while u.getWait():
                    camera_update()
            elif get_object_center_x(0, 0) < 100:
                print "left"
                count += 1
                x.drive_timed(30, -30, .01)
                u.setWait(.3)
                while u.getWait():
                    camera_update()
            else:
                print "found it in " + str(100 - tries) + " tries"
                print(get_object_center_x(0, 0))
                print(get_object_area(0, 0))
                return True
        else:
            print "i see nothing"
            tries -= 1
            msleep(10)
    return False

def square_up():
    global count
    while count != 0:
        if count > 0:
            count -= 1
            x.drive_timed(-30, 30, .01)
        else:
            count += 1
            x.drive_timed(30, -30, .01)
    x.drive_speed(-15, 50)


#Grabs the blue cow and turns to the middle of the board
def grabCowAndGo():
    print "grabCowAndGo"
    if c.isClone:
        x.drive_speed(-5, 20)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
        u.move_servo(c.servoCowArm, c.cowArmStart, 10)
    else:
        msleep(200)
        x.drive_speed(-10, 80)  # was 20
        msleep(200)
        x.rotate(2, 10)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 80)
        u.move_servo(c.servoCowArm, c.cowArmTurn, 20)

def goToStartBox():
    x.ADJUST = 1.05  # straighter drive, didn't want to mess up earlier values
    x.drive_speed(54, 100)
    x.drive_condition(100, 100, u.seeBlackLeft, False)
    x.pivot_right(45, 50)
    x.drive_speed(5, 50)
    x.pivot_right(45, 50)
    x.drive_speed(17, 80)
    x.drive_speed(-3, 50)
    x.pivot_left(-90, 85)
    x.drive_speed(-8, 50)
    u.move_servo(c.servoArm, c.armUpRampBotGuy, 10)

#Drives the Robot to the terrace
def goToTerrace():
    x.drive_speed(23, 60)
    x.line_follow_ramp(37)
    x.line_follow_terrace(12)


#Scores Botguy and the blue cow on the terrace
def scoreOnTerrace():
    msleep(300)
    u.move_servo(c.servoCowArm, c.cowArmDrop)
    msleep(500)
    x.rotate(15, 25)
    msleep(500)
    u.move_servo(c.servoCowClaw, c.cowClawOpen)
    msleep(500)
    u.move_servo(c.servoCowArm, c.cowArmStart)
    msleep(500)
    u.move_servo(c.servoArm, c.armUpRampBotGuyLowered)
    msleep(500)
    x.rotate(-38, 25)     #was -35
    x.drive_speed(1.75, 88)
    x.pivot_left_condition(100, u.seeBlackRight)
    u.move_servo(c.servoCowClaw, c.cowClawClose)
    u.move_servo(c.servoCowArm, c.armDown)
    u.move_servo(c.servoCowArm, c.cowArmDown)
    u.move_servo(c.servoCowClaw, c.cowClawPush)
    #x.rotate(-5, 20)
    print "did it work?"
    u.DEBUGwithWait()


def jump():
    # u.set_servo_position(c.servoArm, c.armDown)
    # u.set_servo_position(c.servoClaw, c.clawOpen)
    # enable_servos()
    #
    # u.waitForButton()
    # u.set_servo_position(c.servoClaw, c.clawClose)
    # msleep(300)

    x.drive_speed(28, 100)
    x.rotate(90, 50)    #faces wall
    u.move_servo(c.servoArm, c.armUpRampBotGuy, 10)
    x.drive_speed(-15, 100) #back wheel over
    x.drive_speed(3, 50)
    x._drive(-100, -100)    #drives backwards for...
    # u.move_servo(c.servoArm, 1900, 2)
    set_servo_position(c.servoArm, 0)  #shifts gravity

    # count = 0
    # while not u.seeBlackLeft():
    #     pass
    # while count < 3:
    #     if u.seeBlackLeft():
    #         count = 0
    #         print "Saw black"
    #     else:
    #         count += 1
    #         print "Saw whyte"
    #     msleep(50)

    while magneto_x() < 10:
        pass
    while magneto_x() > 0:
        pass
    msleep(300)

    #msleep(2000)    #.... this amount of time
    u.move_servo(c.servoArm, get_servo_position(c.servoArm) + 300)
    msleep(100)
    u.move_servo(c.servoArm, get_servo_position(c.servoArm) - 300)
    x.drive_speed(15, 100)    #squareup  #was 24

#################################### Merged Code ####################################
def alt_init():
    print "init"
    if c.isClone:
        print "i am clone"
    else:
        print "i am prime"
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armDown, 100)
    u.move_servo(c.servoCowClaw, c.cowClawOpen, 100)
    u.move_servo(c.cowArm, c.cowArmDown, 100)
    enable_servos()
    u.waitForButton()
    c.startTime = seconds()
    u.move_servo(c.servoClaw, c.clawClose, 45)
    msleep(500)
    u.move_servo(c.servoArm, c.armUpBotguy, 45)
    camera_open()


def alt_grabCowAndGo():
    print "grabCowAndGo"
    u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
    u.move_servo(c.cowArm, c.cowArmStart, 10)


# Seeding Code
def toOtherSide():
    print "toOtherSide"
    if c.isClone:
        x.drive_speed(35, 85)
    else:
        x.drive_speed(39, 85)

    x.rotate(-84, 30)
    x.drive_speed(34, 80)
    if c.isClone:
        x.drive_timed(-80, -10, 1.5)
        u.move_servo(c.cowArm, 1000)
        x.drive_timed(-80, -10, .8)
        u.move_servo(c.servoArm, c.armBotguy, 10)
    else:
        x.drive_speed(-3, 30)
        x.pivot_right(45, 30)
        u.move_servo(c.servoArm, c.armBotguy, 10)
        x.drive_timed(-75, -20, 2)
        u.move_servo(c.cowArm, 1000)
    x.drive_speed(-20.0, 45)
    u.move_servo(c.servoArm, c.armUpBotguy, 15)
    x.drive_speed(-4, 45)

    # u.move_servo(c.servoArm, c.armBotguy, 10)
    x.pivot_right(90, 100)

    u.waitForButton()
    x.pivot_right(43, 60)
    x.drive_speed(7.5, 30)
    x.drive_speed(-24, 50)


def driveToCow2():
    x.drive_speed(-22, 50)  #was -24
    x.rotate(109, 25)   #was 100
    u.move_servo(c.servoCowArm, c.cowArmStart)
    x.drive_speed(-25, 85)
    # x.drive_timed(-20, -25, 2)
