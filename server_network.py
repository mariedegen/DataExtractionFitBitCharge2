from bluetooth import *

//Non-privileged port
port = 8888 
bluetooth_MAC_address = "B8-81-98-D4-F2-78"

server_socket = BluetoothSocket(RFCOMM)
server_socket.bind((bluetooth_MAC_address, port))
server_socket.listen(1)

while True:
    client_socket, address = server_socket.accept()
    try:
        while True:
            data = client_socket.recv(1024)
            if data:
                print "received [%s]" %data
				client_socket.send(data)
			else if not data : break
			
    except:
        print("Closing socket")
        client_socket.close()
		server_socket.close()