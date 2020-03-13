import socket


msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_sock.bind(('', 9090))

print("UDP server up and listening")

while True:
    bytesAddressPair = my_sock.recvfrom(1024)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client

    my_sock.sendto(bytesToSend, address)