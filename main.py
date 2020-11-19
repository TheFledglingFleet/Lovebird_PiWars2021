# Lovebird Main #
# Version 0.1 #
# imports #
import pyfirmata
from inputs import get_gamepad
 
# Set up Variable
comp = { "left": {
            "power": 0, 
        "direction": 0, 
        "powerPin": 2 , 
        "dirPin":22 }, 
      "right": { 
        "power": 0, 
        "direction": 0, 
        "powerPin": 3 , 
        "dirPin":23 } 
    } 
 
# Connect Arduino Board #
board = pyfirmata.Arduino('/dev/ttyACM0')
leftPower = board.get_pin("d:2:p")
rightPower = board.get_pin("d:3:p")
leftDir = board.get_pin("d:22:o")
rightDir = board.get_pin("d:23:o")
 
# Run Code Until Interruption #
while 1:
    # Get Gampad Input #
    events = get_gamepad()
    print(comp)
    for event in events:
    #print(event.ev_type, event.code, event.state)
        if event.code == "ABS_Y":
            comp["left"]["power"] = abs(event.state - 127) * 2
            if (event.state >= 127 ):
                comp["left"]["direction"] = 1
            else:
                comp["left"]["direction"] = 0
                 
        if event.code == "ABS_RZ":
            comp["right"]["power"] = abs(event.state - 127) * 2
            if (event.state > 127 ):
                comp["right"]["direction"] = 1
            else:
                comp["right"]["direction"] = 0
                 
    # Write to Arduino
    leftPower.write( comp["left"]["power"] / 255)
    leftDir.write(comp["left"]["direction"])
 
    rightPower.write( comp["right"]["power"]  / 255)
    rightDir.write(comp["right"]["direction"])