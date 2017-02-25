#!/usr/bin/python

import actions as act

seeding = True

def main():
    print "running"
    act.init()
    act.getBotGuy()
    act.goToCow()
    act.grabCowAndGo()
    if seeding:
        act.toOtherSide()
    act.upRamp()

if __name__ == "__main__":
    main()