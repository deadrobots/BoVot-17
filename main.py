#!/usr/bin/python

import actions as act
from utils import DEBUGwithWait
seeding = True

def main():
    print "running"

    # act.jump()
    # DEBUGwithWait()

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
        DEBUGwithWait()
    act.goToStartBox()
    act.goToTerrace()
    act.scoreOnTerrace()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()