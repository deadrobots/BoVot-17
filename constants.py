'''
Created on Jan 3, 2016
@author: graysonelias
'''

import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 0
RMOTOR = 3
COWMOTOR = 1

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)


# Servos
servoArm = 0
cowArm = 1  #up down
servoClaw = 2
servoCowClaw = 3



armUp = 1400
armUpBotguy = 800
armUpLineFollow = 550
armBotguy = 1800
armDown = 1850

cowDown = 0
cowMid = 0
cowUp = 0
cowArmStart = 500

clawClose = 950
clawOpen = 2047

cowClawOpen = 400
cowClawClose = 1500
cowClawStart = 800

outriggerMid = 1605
outriggerSafe = 1250
outriggerIn = 1950
outriggerOut = 370
outriggerFront = 60 #NEEDS TO BE ADJUSTED FOR PRIME

#Tophat values
FRONT_TOPHAT = 0
frontLineFollowerGrey = 1300

if isClone:
    # Servos
    servoArm = 0
    outrigger = 1
    servoClaw = 2
    servoCowClaw = 3

    armUp = 1500
    armUpBotguy = 900
    armBotguy = 1470
    armDown = 1850



    clawClose = 900
    clawOpen = 1900

    cowClawOpen = 400
    cowClawClose = 1550

    outriggerMid = 1605
    outriggerSafe = 1250
    outriggerIn = 1800
    outriggerOut = 508
    outriggerFront = 0
    #outriggerOutLess = 550
    outriggerInMore = 1900
    outriggerLineFollow = 1580

    # Tophat values
    FRONT_TOPHAT = 0
    frontLineFollowerGrey = 1300