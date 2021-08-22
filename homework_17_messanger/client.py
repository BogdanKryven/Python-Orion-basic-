import re
import json
import socket
import threading


class NickNameError(Exception):
    pass


def json_nicks():
    nicks = []
    for nick in json.load(open("data.json"))["info"]:
        nicks.append(nick)
    return nicks


def read_sock():
    # with open("data.json", "r") as json_data:
    #     data_ = json.load(json_data)
    #
    # while True:
    #     if
    #
    while True:
        data = sock.recv(1024).decode('utf-8')
        print(data)
        try:
            user_nickname = re.search("\[(.*)\]", data).group(0)
        except AttributeError:
            user_nickname = ''
        if user_nickname not in blocked_users_:
            print(data)
        else:
            message_ = "@" + recipient + ", " + " you blocked by this user: "
            sock.sendto((message_ + '[' + alias + '] ').encode('utf-8'), server)


server = ('192.168.1.5', 6002)
alias = input("Your username: ")
all_users = list()
print(all_users)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.sendto(("[" + alias + "] Connect to server").encode('utf-8'), server)

potik = threading.Thread(target=read_sock)
potik.start()

blocked_users_ = list()
while True:
    print('1. Send message to group chat')
    print('2. Send private message')
    print('3. Block user')
    try:
        menu_choose = int(input('Input your choose: '))
    except ValueError:
        continue

    if menu_choose == 1:
        message = input("Your message: ")
        sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
    elif menu_choose == 2:
        recipient = input('Recipient(Nickname): ')
        message = input("Your message: ")
        message = "@" + recipient + ", " + message
        sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
    elif menu_choose == 3:
        recipient = input('Which user you want to block ? (Nickname): ')
        blocked_users_.append("[" + recipient + "]")
        print("User " + recipient + " blocked!")
