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

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)


# Servos
servoArm = 0
outrigger = 1
servoClaw = 2
servoCowClaw = 3



armUp = 580
armUpBotguy = 0
armBotguy = 530
armDown = 920

cowDown = 2047
cowMid = 1700
cowUp = 800

clawClose = 550
clawOpen = 1400

cowClawOpen = 400
cowClawClose = 1550

outriggerMid = 1605
outriggerSafe = 1250
outriggerIn = 1950
outriggerOut = 430

#Tophat values
FRONT_TOPHAT = 0
frontLineFollowerGrey = 1300