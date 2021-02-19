import inputs
import pyfirmata
from inputs import get_gamepad
import time

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
        elif (robotName == "TJ"):
            self.ena = board.get_pin("d:2:p")
            self.in1 = board.get_pin("d:51:o")
            self.in2 = board.get_pin("d:50:o")
            self.in3 = board.get_pin("d:52:o")
            self.in4 = board.get_pin("d:53:o")
            self.enb = board.get_pin("d:3:p")
            
    def drive(self, left, right): #values between 0, 255
        if self.name == "Lovebird":
            leftMotor = int(abs(left - 127) * 2)/255
            rightMotor = int(abs(right - 127) * 2)/255
            
            print(leftMotor, rightMotor)
            if left > 127:
                self.leftDir.write(1)
            else: 
                self.leftDir.write(0)
        
            if right > 127:
                self.rightDir.write(1)
            else: 
                self.rightDir.write(0)
            
            self.leftPower.write(leftMotor)
            self.rightPower.write(rightMotor)
            
        elif self.name == "Tessle":
            self.leftPower.write( int( (leftMotor/255) *180) )
            self.rightPower.write( abs( 180 - int( (rightMotor/255) *180) ) )
        
        elif self.name == "TJ":
            maxSpeed = 60
            maxDivision = 255/maxSpeed
            leftMotor = int(((left - 127) * 2)/maxDivision)
            rightMotor = int(((right - 127) * 2)/maxDivision)
            print(leftMotor, rightMotor)
            if (rightMotor < 0):
                self.in3.write(0)
                self.in4.write(1)
                self.enb.write(rightMotor * -1)
            elif (rightMotor >= 0):
                self.in3.write(1)
                self.in4.write(0)
                self.enb.write(rightMotor)
            
            if (leftMotor < 0):
                self.in1.write(1)
                self.in2.write(0)
                self.ena.write(leftMotor * -1)
            elif (leftMotor >= 0):
                self.in1.write(0)
                self.in2.write(1)
                self.ena.write(leftMotor)
            

myRobot = Lovebird("TJ")
left, right = 0, 0

while 1:
    events = get_gamepad()
    for event in events:
        if event.code == "ABS_Y":
            left = event.state
            
        if event.code == "ABS_RZ":
            right = event.state
    myRobot.drive(left, right) 