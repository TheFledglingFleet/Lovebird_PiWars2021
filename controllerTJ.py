import bluetooth

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
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((target_address, port))

    sock.send("hello!!")

    sock.close()

else:
    print("could not find target bluetooth device nearby")