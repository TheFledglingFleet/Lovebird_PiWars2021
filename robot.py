#Not Currently in use in main, but for future use
import inputs
import pyfirmata

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
        
    def drive(self, leftMotor, rightMotor): #values between -255, 255
        if self.name == "Lovebird":
            left = (leftMotor - 127) * 2
            right = (rightMotor - 127) * 2
            if left > 0:
                leftDir.write(1)
            else: 
                leftDir.write(0)
        
            if right > 0:
                rightMotor.write(1)
            else: 
                rightMotor.write(0)
        
            leftPower.write(abs(left))
            rightPower.write(abs(right))

        elif self.name == "Tessle":
            leftPower.write(leftMotor)
            rightMotor.write(rightMotor)
        
        
    