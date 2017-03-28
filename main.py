#!/usr/bin/python

import actions as act
from utils import DEBUGwithWait, waitForButton, DEBUG
import constants as c

def main():
    # act.jump()
    # DEBUGwithWait()

    c.seeding = act.isSeeding()
    if c.seeding:
        print "running SEEDING"
    else:
        print "running HEAD TO HEAD"
    act.init()
    act.getBotGuy()
    act.goToCow()
    if c.seeding:
        act.findCow()
        act.grabCowAndGo()
        act.square_up()
        act.jump()
        act.driveToCow2()
        act.findCow()
        act.grabCowAndGo2()
        act.square_up2()
        # DEBUGwithWait()
    else:
        act.grabCowAndGo()
        act.squareUpSideHeadToHead()
    act.goToStartBox()
    act.goToTerrace()
    act.scoreOnTerrace()
    DEBUG()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()