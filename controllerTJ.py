import bluetooth
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
    c = BluetoothClient("00:00:12:06:53:92", data_received)
    c.send("ON")

else:
    print("could not find target bluetooth device nearby")