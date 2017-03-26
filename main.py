#!/usr/bin/python

import actions as act
from utils import DEBUGwithWait, waitForButton

def main():
    # act.jump()
    # DEBUGwithWait()

    seeding = True # act.isSeeding()
    if seeding:
        print "running SEEDING"
    else:
        print "running HEAD TO HEAD"
    act.init()
    act.getBotGuy()
    act.goToCow()
    act.findCow()
    act.grabCowAndGo()
    act.square_up()
    if seeding:
        act.jump()
        act.driveToCow2()
        act.findCow()
        act.grabCowAndGo2()
        act.square_up2()
        # DEBUGwithWait()
    act.goToStartBox()
    act.goToTerrace()
    act.scoreOnTerrace()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()