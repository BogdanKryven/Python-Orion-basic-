from __future__ import annotations
import re
import json
import socket
import threading

clients_ = list()


def open_json_data():
    try:
        with open("data.json", "r") as json_data:
            data_ = json.load(json_data)
            for i in data_["info"]:
                clients_.append(i["nickname"])
    except json.decoder.JSONDecodeError:
        pass


def read_sock():
    while True:
        data = sock.recv(1024).decode('utf-8')
        try:
            user_nickname = re.search("\[(.*)\]", data).group(0)
        except AttributeError:
            user_nickname = ''
        if user_nickname not in blocked_users_:
            print(data)
        else:
            message = "@" + recipient + ", " + " you blocked by this user"
            sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)


def input_username():
    alias_ = input("Your username: ")
    if "[" + alias_ + "]" in clients_:
        while True:
            print("This nickname is already used. Try again")
            alias_ = input("Your new username: ")
            if "[" + alias_ + "]" not in clients_:
                break
            else:
                continue
    return alias_


server = ('0.0.0.0', 6002)
open_json_data()
alias = input_username()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
