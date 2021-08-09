import json


class NamesError(Exception):
    pass


class EmailError(Exception):
    pass


def add_info():
    try:
        data = json.load(open("data.json"))
    except:
        data = {"info": []}

    users = {
        "name": f"{input('Input your name: ')}",
        "email": f"{input('Input your email: ')}"
    }

    names = []
    for name in data["info"]:
        names.append(name["name"])

    emails = []
    for email in data["info"]:
        emails.append(email["email"])

    if users.get("name") in names:
        raise NamesError
    elif users.get("email") in emails:
        raise EmailError
    else:
        data["info"].append(users)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


for _ in range(int(input(f"How many users you want to add? "))):
    try:
        add_info()
    except NamesError:
        print("This name is already in dictionary!\n")
    except EmailError:
        print("This email is already in dictionary!\n")
