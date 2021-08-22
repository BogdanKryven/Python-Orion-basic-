from __future__ import annotations
import re
import json
import socket
import threading
from time import sleep


class NickNameError(Exception):
    pass


try:
    with open("data.json", "r") as json_data:
        data_ = json.load(json_data)
except json.decoder.JSONDecodeError:
    data_ = {"info": []}

nicks_ = list()
for i in data_["info"]:
    nicks_.append(i["nickname"])
print(nicks_)


def read_sock():
    # while True:
    #     if alias in nicks_:
    #         print("This nickname is already used. Try again.")
    #         alias_ = input("Input your new nickname: ")
    #         if alias_ in nicks_:
    #             break
    #         else:
    #             sock.sendto(("[" + alias + "] Connect to server").encode('utf-8'), server)
    #             break
    #     else:
    #         break

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


server = ('0.0.0.0', 6002)
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
    sleep(0.2)
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
