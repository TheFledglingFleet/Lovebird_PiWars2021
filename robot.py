#Not Currently in use in main, but for future use

import inputs
import pyfirmata

class Lovebird():

    def __init__(self):
        board = pyfirmata.ArduinoMega('/dev/ttyACM0')
        self.leftPower = board.get_pin("d:2:p")
        self.rightPower = board.get_pin("d:22:p")
        self.leftDir = board.get_pin("d:3:o")
        self.rightDir = board.get_pin("d:23:o")
    
    def drive(leftMotor, rightMotor): #values between -255, 255
        if leftMotor > 0:
            leftDir.write(1)
        else: 
            leftDir.write(0)
        
        if rightMotor > 0:
            rightMotor.write(1)
        else: 
            rightMotor.write(0)
        
        leftPower.write(abs(leftMotor))
        rightPower.write(abs(rightMotor))
        
    