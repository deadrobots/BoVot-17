import motorsPlusPlus as x
import utils as u
import constants as c

from wallaby import *
import sys


def squareUpSideHeadToHead():
    x.drive_speed(16, 100)
    x.rotate(90, 50)
    x.drive_speed(-16, 100)
    msleep(4000)
    x.drive_speed(12, 100)
    x.rotate(-80, 25)

def isSeeding():
    seeding = False
    while True:
        print("For SEEDING press the LEFT (inside) button.")
        print("For HEAD TO HEAD press the RIGHT (outside) button.")

        while right_button() or left_button():
            pass

        while not right_button() and not left_button():
            pass
        if right_button():
            print("\nYou have selected HEAD TO HEAD")
            # print("Press and hold both buttons to confirm your selection...")
            seeding = False
        else:
            print("\nYou have selected SEEDING")
            # print("Press and hold both buttons to confirm your selection...")
            seeding = True
        while right_button() or left_button():
            pass
        return seeding

        # while right_button() or left_button():
        #     pass
        # print("Do nothing for 5 seconds to cancel...")
        # start_time = seconds()
        # cont = True
        # while not right_button() or not left_button():
        #     if seconds() > start_time + 5:
        #         cont = False
        #         break
        # if cont:
        #     start_time = seconds()
        #     print("")
        #     while right_button() and left_button():
        #         if seconds() > start_time + 3:
        #             print("\n\nOK")
        #             return seeding
        #         else:
        #             out = "\r["
        #             progress = (start_time + 3 - seconds()) / 3.0
        #             for _ in range (0, 10-int(progress * 10)):
        #                 out += "|"
        #             for _ in range (0, int(progress * 10)):
        #                 out += " "
        #             out += "]"
        #             # sys.stdout.write(out)
        #             # sys.stdout.flush()
        #             msleep(10)
        # print("Canceled!\n\n\n")


    # while True:
    #     print("Select run style below:")
    #     set_a_button_text("Seeding")
    #     set_b_button_text("")
    #     set_c_button_text("Head to Head")
    #
    #     while not a_button_clicked() and not b_button_clicked():
    #         pass
    #     if a_button_clicked():
    #         seeding = True
    #         print("You selected SEEDING.\nConfirm your selection below:")
    #     elif b_button_clicked():
    #         seeding = False
    #         print("You selected HEAD TO HEAD.\nConfirm your selection below:")
    #     else:
    #         print("Error, run again!")
    #         exit(0)
    #     while a_button_clicked() or b_button_clicked:
    #         pass
    #     set_a_button_text("Ok")
    #     set_b_button_text("")
    #     set_c_button_text("Cancel")
    #     if a_button_clicked:
    #         print("OK")
    #         return seeding
    #     else:
    #         print("Canceled")

# Tests all of the actuators and sensors
def init():
    print "init"
    if c.isClone:
        print "i am clone"
    else:
        print "i am prime"
    enable_servos()
    u.start_up_test()
    u.move_servo(c.servoClaw, c.clawClose, 100)
    u.move_servo(c.servoArm, c.armUpLineFollow, 100)
    u.move_servo(c.servoCowClaw, c.cowClawStart, 100)
    u.move_servo(c.servoCowArm, c.cowArmUp, 100)
    # u.position()
    # u.waitForButton()
    u.wait4light()
    shut_down_in(119.9)
    c.startTime = seconds()


# Drives out of the start box and gets Botguy from the aquifer
def getBotGuy():
    print "getBotGuy"
    # Get out of start box

    x.arc_radius(5,90,100)
    x.drive_speed(18,100)
    msleep(100)
    if c.isClone:
        x.rotate(-57,50)     #use to -45
    else:
        x.rotate(-47, 50)
    x.drive_speed(5, 70)
    x.find_pole()
    x.drive_speed(1.5, 40)
    x.pivot_right(93, 60)  #used to be 90
    x.drive_speed(9, 70) # was 7
    x.drive_speed(-6, 60)  #used to be -6
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armDown, 20)
    x.drive_speed(10, 50)
    u.move_servo(c.servoClaw, c.clawClose, 100)  # grab botguy
    u.move_servo(c.servoArm, c.armUp, 10)


    if c.seeding:
        if c.isClone:
            x.drive_speed(5, -40)
        else:
            x.drive_speed(4, -40)  # was 6
        u.move_servo(c.servoArm, c.armUpBotguy, 10)
        x.drive_speed(4.5, -60)
    else:
        x.drive_speed(-4, 100)
        u.move_servo(c.servoArm, c.armUpBotguy, 15)
        x.drive_speed(5, 100)
        msleep(7000)
        if c.isClone:
            x.drive_speed(5, -40)
            x.drive_speed(4.5, -60)
        else:
            x.drive_speed(4, -40)    #was 6
            x.drive_speed(4.5, -60)


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
        x.rotate(-10, 20)
    else:
        x.pivot_right(-81, 75)  # was 30
        x.drive_speed(12, 80)  # was 40
        x.rotate(175, 25)  # was 172
        if c.seeding:
            x.ADJUST = 1.00
        u.move_servo(c.servoCowArm, c.cowArmDown, 20)
        u.move_servo(c.servoCowClaw, c.cowClawOpen, 20)
        x.rotate(-7, 20)
        x.drive_speed(8, -80)

def driveToCow2():
    u.move_servo(c.servoCowArm, c.cowArmUp)
    x.drive_speed(-16, 85)
    x.rotate(91, 30)
    x.drive_speed(-23, 85)
    x.rotate(-90, 30)
    x.drive_speed(12, 100)
    x.drive_speed(-12.5, 100)
    x.rotate(85, 30)
    # x.drive_speed(-5, 100)


count = 0

# Uses the camera to locate the blue cow
def findCow():
    turns = 3
    camera_open()
    for _ in range(0, turns):
        if center_on_cow():
            break
        print "rotating"
        x.rotate(10, 30)
    camera_close()

def center_on_cow():
    camera_open()
    global count
    tries = 30
    for _ in range(0, 10):
        camera_update()
        msleep(25)
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
                print "found it in " + str(30 - tries) + " tries"
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
    if c.seeding:
        x.drive_speed(-25, 100)
    else:
        x.drive_speed(-20, 100)


#Grabs the blue cow and turns to the middle of the board
def grabCowAndGo():
    print "grabCowAndGo"
    if c.isClone:
        x.drive_speed(-8, 80)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
        u.move_servo(c.servoCowArm, c.cowArmUp, 10)
        x.ADJUST = 0.98
    else:
        if c.seeding:
            x.drive_speed(-5, 80)  # was 20
        else:
            x.drive_speed(-5, 80)
        # x.rotate(6, 60)   to be continued...
        x.rotate(3.5, 10) #rotate to grab Cow
        u.move_servo(c.servoCowClaw, c.cowClawClose, 40)
        u.move_servo(c.servoCowArm, c.cowArmUp, 20)

def goToStartBox():
    # x.ADJUST = 1.04 #was 1.05  # straighter drive, didn't want to mess up earlier values
    if c.seeding:
        x.drive_speed(50, 100)
    else:
        x.drive_speed(20, 100)
    if c.isClone:
        state = x.drive_speed_saw_black(45, 100)
    else:
        state = x.drive_speed_saw_black(40, 100)
    if state == 0:
        x.drive_condition(-100, -100, u.seeBlackLeft)
        x.drive_condition(-100, -100, u.seeBlackRight)
        x.rotate(45, 50)
        x.drive_speed(16, 50)
        x.rotate(-30, 50)
        x.drive_speed(12, 100)
    elif state == 2:
        x.drive_speed(-12, 50)
        x.rotate(45, 50)
        x.drive_speed(12, 50)
        x.rotate(-30, 50)
        x.drive_speed(6, 100)
    x.drive_speed(-5, 60)
    x.pivot_right(-90, 60)
    x.drive_speed(-20, 80)
    x.pivot_left(90, 60)
    if c.seeding:
        x.drive_speed(-10, 50)
    else:
        if c.isClone:
            x.drive_speed(-10, 50)
        else:
            x.drive_speed(-8, 50)
    u.move_servo(c.servoArm, c.armUpRampBotGuy, 10)
    u.move_servo(c.servoCowArm, c.cowArmUp, 10)

#Drives the Robot to the terrace
def goToTerrace():
    x.drive_speed(18, 60)      #was 23
    u.move_servo(c.servoArm, c.armOnRampBotGuy, 10)
    x.line_follow_ramp(37)
    if c.seeding:
        x.line_follow_terrace(15)
    else:
        x.line_follow_terrace(15)
    x.drive_speed(-1, 100)

#Scores Botguy and the blue cow on the terrace
def scoreOnTerrace():
    # if c.seeding:
    #     msleep(300)
    #     u.move_servo(c.servoCowArm, c.cowArmDrop)
    #     u.move_servo(c.servoCowClaw, c.cowClawOpen)
    #     u.move_servo(c.servoCowArm, c.cowArmUp)
    #     x.rotate(15, 65)
    #     u.move_servo(c.servoCowArm, c.cowArmDown)
    #     x.rotate(-20, 70)
    #     x.rotate(-38, 25)  # was -35
    #     x.pivot_right(-10, 50)  # was -100
    #     u.move_servo(c.servoArm, c.armUpRampBotGuyLowered)
    #     u.move_servo(c.servoCowClaw, c.cowClawClose)
    #     u.move_servo(c.servoCowArm, c.armDown)
    #     u.move_servo(c.servoCowArm, c.cowArmDown)
    #     u.move_servo(c.servoCowClaw, c.cowClawPush)
    # else:

    u.move_servo(c.servoCowArm, c.cowArmDrop)
    x.rotate(15, 25)
    u.move_servo(c.servoCowClaw, c.cowClawOpen)
    x.drive_speed(1.5, 50) # caitlyns code
    x.drive_speed(-1.5, 50) # caitlyns code
    u.move_servo(c.servoCowArm, c.cowArmUp)
    x.rotate(-38, 50)     #was -35
    x.pivot_right(-10, 50)    #was -100
    u.move_servo(c.servoArm, c.armUpRampBotGuyLowered, 100)
    u.move_servo(c.servoCowClaw, c.cowClawClose, 100)
    u.move_servo(c.servoCowArm, c.cowArmDown, 100)
    u.move_servo(c.servoCowClaw, c.cowClawPush, 100)
    #x.rotate(-5, 20)

magneto_ground = 0

def jump():
    # msleep(3000)
    x.drive_speed(28, 100) #was 28
    u.move_servo(c.servoCowArm, c.cowArmTurn)
    x.rotate(90, 50)    #faces wall

    # u.set_servo_position(c.servoArm, c.armDown)
    # u.set_servo_position(c.servoClaw, c.clawOpen)
    # u.move_servo(c.servoCowArm, c.cowArmTurn)
    # enable_servos()

    # u.waitForButton()
    # u.set_servo_position(c.servoClaw, c.clawClose)
    # msleep(500)
    # u.set_servo_position(c.servoArm, c.armUpLineFollow)
    # msleep(300)

    x.drive_speed(-12, 80)

    x.drive_power(-50, -50)
    u.set_servo_position(c.servoArm, c.armBotguyHover)
    msleep(1500)

    x.drive_power(-100, -100)  # drives backwards for...
    # u.set_servo_position(c.servoCowArm, 1000)
    # u.move_servo(c.servoArm, 1900, 2)
    set_servo_position(c.servoArm, 0)  # shifts gravity
    msleep(2000)
    # u.set_servo_position(c.servoCowArm, 800)
    # x.drive_speed(16, 100)

    # u.move_servo(c.servoArm, c.armUpRampBotGuy, 10)
    # x.drive_speed(-15, 100) #back wheel over

    x.drive_speed(16, 100)

    while False:
        x.drive_speed(3, 50) #straddle square up
        x.drive_power(-100, -100)    #drives backwards for...
        # u.move_servo(c.servoArm, 1900, 2)
        set_servo_position(c.servoArm, 0)  #shifts gravity
        u.setWait(2.5)
        while u.getWait():
            pass
        print "swinging"
        x.drive_speed(16, 100)    #squareup  #was 24
        x.pivot_left(4, 30)
        x.pivot_right(4, 30)
        x.drive_power(60, 60)
        if analog(c.TOPHAT_PIPE) > 2000:
            x.freeze_motors()
            break
        else:
            u.move_servo(c.servoArm, c.armUpRampBotGuy, 10)



def square_up2():
    #global count
    #while count != 0:
    #    if count > 0:
    #        count -= 1
    #        x.drive_timed(-30, 30, .01)
    #    else:
    #        count += 1
    #        x.drive_timed(30, -30, .01)
    x.drive_speed(-20, 100)
    msleep(1000)


#Grabs the blue cow and turns to the middle of the board
def grabCowAndGo2():
    print "grabCowAndGo"
    u.move_servo(c.servoCowArm, c.cowArmDown)
    u.move_servo(c.servoCowClaw, c.cowClawOpen)
    x.rotate(-2, 25)
    x.drive_speed(-8, 100)
    if c.isClone:
        x.drive_speed(-5, 20)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 10)
        u.move_servo(c.servoCowArm, c.cowArmUp, 10)
    else:
        # msleep(200)
        # x.drive_speed(-10, 80)  # was 20
        # msleep(200)
        x.rotate(2, 10)
        u.move_servo(c.servoCowClaw, c.cowClawClose, 40)
        u.move_servo(c.servoCowArm, c.cowArmTurn, 20)
        x.ADJUST = 1.04
        # msleep(5000)