from inputs import get_gamepad
from robot import Lovebird

myRobot = Lovebird("Tessle")

while 1:
    events = get_gamepad()
    left, right = 0, 0
    for event in events:
        if event.code == "ABS_Y":
            left = event.state
            
        if event.code == "ABS_RZ":
            right = event.state
    myRobot.drive(left, right) 
