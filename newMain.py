from inputs import get_gamepad
import robot

myRobot = robot.Lovebird("Tessle")
left, right = 0, 0

while 1:
    events = get_gamepad()
    for event in events:
        if event.code == "ABS_Y":
            left = event.state
            
        if event.code == "ABS_RZ":
            right = event.state
    myRobot.drive(left, right) 
