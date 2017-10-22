from bluetooth import *


def serverNetwork(port, bluetooth_MAC_address):
##    //Non-privileged port
##    port = 8888 
##    bluetooth_MAC_address = "B8-81-98-D4-F2-78"

    tabData = []

    server_socket = BluetoothSocket(RFCOMM)
    server_socket.bind((bluetooth_MAC_address, port))
    server_socket.listen(1)

    while True:
        client_socket, address = server_socket.accept()
        try:
            while True:
                data = client_socket.recv(1024)
                if data:
                    print("received [%s]" %data)
                    tabData.append(data)
                    client_socket.send(data)
                elif not data :
                    break
                            
        except:
            print("Closing socket")
            client_socket.close()
            server_socket.close()

    return tabData

		
