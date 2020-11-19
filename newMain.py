# New Main #
import pyfirmata
from inputs import get_gamepad
from robot import Lovebird

myRobot = Lovebird()

while 1:
    events = get_gamepad()
    left, right = 0, 0
    for event in events:
        if event.code == "ABS_Y":
            left = (event.state - 127) * 2
            
        if event.code == "ABS_RZ":
            right = (event.state - 127) * 2
    myrobot.drive(left, right) 
