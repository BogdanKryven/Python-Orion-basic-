import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 9090))
server_socket.listen()

while True:
    client_socket, address = server_socket.accept()
    print("connect", address)
    while True:
        request_data = client_socket.recv(4096)
        if not request_data:
            break
        print(request_data.decode())
        response = "OK"
        client_socket.send(response.encode())
