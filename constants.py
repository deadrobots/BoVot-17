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
LEFT_BUTTON = 0
RIGHT_BUTTON = 1
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)

# Servos
servoArm = 0
servoCowArm = 1
servoClaw = 2
servoCowClaw = 3

#Main Arm Values
armUp = 900#1400
armUpBotguy = 300#800
armOnRampBotGuy = 1100#1500  # 1575
armUpRampBotGuy = 860#1500  # 1575
armUpRampBotGuyLowered = 1300#1800
armUpLineFollow = 50#550
armBotguy = 1300#1800
armDown = 1350#1850
armBotguyHover = 800#1300

#Cow Arm values
cowArmDown = 1800
cowArmStart = 600
cowArmTurn = 1270
cowArmDrop = 1550

#Botguy Claw Values
clawClose = 450
clawOpen = 2000

#Cow Claw Values
cowClawOpen = 1800
cowClawPush = 1900
cowClawClose = 1000
cowClawStart = 1400

# Tophat values
frontLineFollowerGrey = 1300
ET = 5
TOPHAT_PIPE = 3
STARTLIGHT = 4

if isClone:
    # Servos
    servoArm = 0
    servoCowArm = 1
    servoClaw = 2
    servoCowClaw = 3

    #Main Arm Values
    armUp = 1500
    armUpBotguy = 900
    armBotguy = 1470
    armDown = 1850
    armUpRampBotGuy = 1500
    armUpRampBotGuyLowered = 1800
    armUpLineFollow = 550
    armBotguy = 1800
    armDown = 1850
    armBotguyHover = 1300

    # Cow Arm values
    cowArmDown = 1800
    cowArmStart = 600
    cowArmTurn = 1270
    cowArmDrop = 1550

    #Botguy Claw Values
    clawClose = 900
    clawOpen = 1900

    #Cow Claw Values
    cowClawOpen = 1550
    cowClawPush = 1900
    cowClawClose = 900
    cowClawStart = 1650



    # Tophat values
    FRONT_TOPHAT = 0
    frontLineFollowerGrey = 1300
