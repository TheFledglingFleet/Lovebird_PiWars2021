import bluetooth
from inputs import get_gamepad
from bluedot.btcomm import BluetoothClient
import time 

class robot():
    def data_received(self, data):
        print(data)
    
    def __init__(self):
        self.target_name = "HC-06"
        self.target_address = None
        port = 3
        
        nearby_devices = bluetooth.discover_devices()
        
        for bdaddr in nearby_devices:
            if self.target_name == bluetooth.lookup_name( bdaddr ):
                self.target_address = bdaddr
                break
        if self.target_address is not None:
            print("found target bluetooth device with address ", self.target_address)
            self.c = BluetoothClient(self.target_address, self.data_received)
            
    def run(self):
        left, right = 0, 0
        while(1):
            time.sleep(0.01)
            events = get_gamepad()
            
            maxSpeed = 40
            maxDivision = 255/maxSpeed
            for event in events:
                if event.code == "ABS_Y":
                    left = ((int(event.state) - 127) * 2)/maxDivision
                
                if event.code == "ABS_RZ":
                    right = ((int(event.state) - 127) * 2)/maxDivision
            value = "<{0},{1}>".format(left, right)
            print(value)
            #self.c.send(value)

if __name__ == "__main__":
    bot = robot()
    bot.run()