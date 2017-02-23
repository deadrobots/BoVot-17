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
servoCow = 1
servoClaw = 2
servoCowClaw = 3


armUp = 580
armUpBotguy = 0
armBotguy = 530
armDown = 920

cowDown = 2047
cowMid = 1700
cowUp = 800

clawClose = 930
clawOpen = 1800

cowClawOpen = 400
cowClawClose = 1550