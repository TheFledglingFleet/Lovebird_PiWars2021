import bluetooth
from inputs import get_gamepad
from bluedot.btcomm import BluetoothClient

target_name = "HC-06"
target_address = None
port = 3

nearby_devices = bluetooth.discover_devices()

def data_received(data):
    print(data)
	
for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
    c = BluetoothClient(target_address, data_received)
    while(1):
        events = get_gamepad()
        left, right = 127, 127
        for event in events:
            if event.code == "ABS_Y":
                left = int(event.state)
                
            if event.code == "ABS_RZ":
                right = int(event.state)
        value = "<{0},{1}>".format(left, right)
        print(value)
        c.send(value)
