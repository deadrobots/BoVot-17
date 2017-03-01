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
outrigger = 1
servoClaw = 2
servoCowClaw = 3



armUp = 1350
armUpBotguy = 800
armUpLineFollow = 445
armBotguy = 1700
armDown = 1700

cowDown = 2047
cowMid = 1700
cowUp = 1250

clawClose = 950
clawOpen = 2047

cowClawOpen = 400
cowClawClose = 1500

outriggerMid = 1605
outriggerSafe = 1250
outriggerIn = 1950
outriggerOut = 450

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
    armBotguy = 1700
    armDown = 1900

    cowDown = 2047
    cowMid = 1700
    cowUp = 1250

    clawClose = 900
    clawOpen = 1900

    cowClawOpen = 400
    cowClawClose = 1550

    outriggerMid = 1605
    outriggerSafe = 1250
    outriggerIn = 1950
    outriggerOut = 930

    # Tophat values
    FRONT_TOPHAT = 0
    frontLineFollowerGrey = 1300