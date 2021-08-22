import socket
import re
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 6002))
clients = {}
nicks = list()
print("Server start")

try:
    with open("data.json", "r") as json_data:
        data_ = json.load(json_data)
except json.decoder.JSONDecodeError:
    data_ = {"info": []}

nicks_ = list()
for i in data_["info"]:
    nicks_.append(i["nickname"])


while True:
    # print("1 - ", clients)
    data, address = sock.recvfrom(1024)
    recipient_nickname = re.search("@(.*),", data.decode('utf-8'))
    # print(address)
    print("\nclients before all", clients.values())
    if recipient_nickname is None:
        # print(nicks_)

        if address not in clients.keys():
            try:
                if clients[address] not in clients.values():
                    clients[address] = re.search("\[(.*)\]", data.decode('utf-8')).group(0)
                else:
                    print("1 - else ", clients.values())
                    sock.sendto("Already registered".encode("utf-8"), address)
                    break
            except KeyError:
                print("\n 2 - key error", clients.values())
                clients[address] = re.search("\[(.*)\]", data.decode('utf-8')).group(0)
                continue

        for client in clients:
            if client == address:
                continue
            sock.sendto(data, client)

    else:
        recipient_nickname = recipient_nickname.group(0)
        recipient_nickname = list(recipient_nickname)
        print(recipient_nickname)
        del recipient_nickname[0]
        del recipient_nickname[-1]
        recipient_nickname = "".join(recipient_nickname)
        for address in clients:
            if clients[address] == "[" + recipient_nickname + "]":
                sock.sendto(data, address)
    nicks = [value.replace('[', '').replace(']', '') for key, value in clients.items()]

    print("else in clients keys ", clients[address])

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
    if users not in data["info"]:
        data["info"].append(users)
    else:
        pass

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


