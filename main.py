#!/usr/bin/python

import actions as act
seeding = False

def main():
    print "running"
    act.init()
    act.getBotGuy()
    act.goToCow()
    act.findCow()
    act.grabCowAndGo()
    act.square_up()
    exit(0)
    if seeding:
        act.toOtherSide()
        act.driveToCow2()
    act.goToStartBox()
    act.goToTerrace()
    act.scoreOnTerrace()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()