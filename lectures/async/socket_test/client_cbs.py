import socket
import selectors

selector = selectors.DefaultSelector()


def init_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 9090))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, address = server_socket.accept()
    print("connect", address)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=get_message)


def get_message(client_socket):
    request_data = client_socket.recv(4096)
    if not request_data:
        selector.unregister(client_socket)
        client_socket.close()
        return
    print(request_data.decode())
    response = "OK"
    client_socket.send(response.encode())


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            cb = key.data
            cb(key.fileobj)


if __name__ == '__main__':
    init_server_socket()
    event_loop()



