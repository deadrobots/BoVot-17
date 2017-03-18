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

# analog ports
LTOPHAT = 0
RTOPHAT = 1

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
armUpRampBotGuy =1500 #1575
armUpRampBotGuyLowered = 1800
armUpLineFollow = 550
armBotguy = 1800
armDown = 1850
botguyHover = 1300

cowDown = 1800
cowArmStart = 345
cowArmTurn = 1270
cowArmDrop = 1550

clawClose = 450
clawOpen = 2000

cowClawOpen =1800
cowClawClose = 1000
cowClawStart = 1400

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
    armUpRampBotGuy = 1500

    clawClose = 900
    clawOpen = 1900

    cowClawOpen = 1550
    cowClawClose = 900
    cowClawStart = 1650

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