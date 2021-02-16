import bluetooth
from inputs import get_gamepad

target_name = "HC-06"
target_address = None
port = 3

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
    c = BluetoothClient(target_address, data_received)
    white(1):
        events = get_gamepad()
            for event in events:
                if event.code == "ABS_Y":
                    left = int(event.state)
            
                if event.code == "ABS_RZ":
                    right = int(event.state)
            c.send("<{0},{1}>".format(left, right))

