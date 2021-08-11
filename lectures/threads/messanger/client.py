import socket
import threading


def read_sock():
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


server = ('192.168.31.242', 5050)
alias = input("Your username: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.sendto((alias + " Connect to server").encode('utf-8'), server)

potik = threading.Thread(target=read_sock)
potik.start()

while True:
    message = input("Your message: ")
    sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)