import socket

socket = socket.socket()

socket.connect(('localhost', 9090))

while True:
    msg = input()
    if msg == "0":
        break

    socket.send(msg.encode())
    request_data = socket.recv(4096)

    print(request_data.decode())


socket.close()

