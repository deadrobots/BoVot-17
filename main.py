#!/usr/bin/python

import actions as act
import utils as u

seeding = True

def main():

    print "running"
    '''
    act.init()
    act.getBotGuy()
    act.goToCow()
    act.findCow()
    act.grabCowAndGo()
    if seeding:
        act.toOtherSide()
    act.upRamp()
    '''
    print"Test"
    act.test()
if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()