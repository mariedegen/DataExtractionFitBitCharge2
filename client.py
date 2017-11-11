import bluetooth

port = 8888 
bluetooth_MAC_address = "B8-81-98-D4-F2-78"

client_socket = BluetoothSocket(RFCOMM)

client_socket.connect((bluetooth_MAC_address, 3))

client_socket.send("Hello World")

print("Finished")

client_socket.close()

