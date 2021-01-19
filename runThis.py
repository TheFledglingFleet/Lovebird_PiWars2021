import inputs
import pyfirmata
from inputs import get_gamepad

class Lovebird():

    def __init__(self, robotName):
        board = pyfirmata.ArduinoMega('/dev/ttyACM0')
        self.name = robotName
        if (robotName == "Lovebird"):
            self.leftPower = board.get_pin("d:2:p")
            self.rightPower = board.get_pin("d:3:p")
            self.leftDir = board.get_pin("d:22:o")
            self.rightDir = board.get_pin("d:23:o")
        elif (robotName == "Tessle"):
            self.leftPower = board.get_pin("d:2:s")
            self.rightPower = board.get_pin("d:3:s")
        
    def drive(self, left, right): #values between 0, 255
        if self.name == "Lovebird":
            leftMotor = abs(leftMotor)
            rightMotor = abs(rightMotor)
            print("Meow")
            print(left, right)
            print("Woof")
            print(leftMotor, rightMotor)
            print("\n")
            
            if left > 0:
                self.leftDir.write(1)
            else: 
                self.leftDir.write(0)
        
            if right > 0:
                self.rightDir.write(1)
            else: 
                self.rightDir.write(0)
        
            self.leftPower.write(int(leftMotor))
            self.rightPower.write(int(rightMotor))
            
        elif self.name == "Tessle":
            self.leftPower.write( int( (leftMotor/255) *180))
            self.rightPower.write( abs( 180 - int( (rightMotor/255) *180) ) )
        
        

myRobot = Lovebird("Lovebird")
left, right = 0, 0

while 1:
    events = get_gamepad()
    for event in events:
        if event.code == "ABS_Y":
            left = event.state
            
        if event.code == "ABS_RZ":
            right = event.state
    myRobot.drive(left, right) 