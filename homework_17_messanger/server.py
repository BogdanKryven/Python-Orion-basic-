import socket
import re
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.5', 6002))
clients = {}
print("Server start")


while True:
    data, address = sock.recvfrom(1024)
    recipient_nickname = re.search("@(.*),", data.decode('utf-8'))
    print(address)
    if recipient_nickname is None:
        if address not in clients.keys():
            clients[address] = re.search("\[(.*)\]", data.decode('utf-8')).group(0)
        for client in clients:
            if client == address:
                continue
            sock.sendto(data, client)
    else:
        recipient_nickname = recipient_nickname.group(0)
        recipient_nickname = list(recipient_nickname)
        del recipient_nickname[0]
        del recipient_nickname[-1]
        recipient_nickname = "".join(recipient_nickname)
        for address in clients:
            if clients[address] == "[" + recipient_nickname + "]":
                sock.sendto(data, address)

    nicks = [value.replace('[', '').replace(']', '') for key, value in clients.items()]
    print(nicks)
    nicks_ = list()
    try:
        for nick in json.load(open("data.json"))["info"]:
            nicks_.append(nick["nickname"])
        data = json.load(open("data.json"))
    except json.decoder.JSONDecodeError:
        data = {"info": []}

    users = {
        "nickname": f"{nicks[-1]}",
    }

    data["info"].append(users)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(nicks)
