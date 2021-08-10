import json
from json_exceptions import NamesEmailError, NamesError, EmailError


def data_name():
    names = []
    for name in json.load(open("data.json"))["info"]:
        names.append(name["name"])
    return names


def data_email():
    emails = []
    for email in json.load(open("data.json"))["info"]:
        emails.append(email["email"])
    return emails


def add_info():
    try:
        data = json.load(open("data.json"))
        names = data_name()
        emails = data_email()
    except json.decoder.JSONDecodeError:
        data = {"info": []}
        names = []
        emails = []

    users = {
        "name": f"{input('Input your name: ')}",
        "email": f"{input('Input your email: ')}"
    }
    if users.get("name") in names and users.get("email") in emails:
        raise NamesEmailError
    elif users.get("name") in names:
        raise NamesError
    elif users.get("email") in emails:
        raise EmailError
    else:
        data["info"].append(users)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# for _ in range(int(input(f"How many users you want to add? "))):
#     try:
#         add_info()
#     except NamesError:
#         print("This name is already in dictionary!\n")
#     except EmailError:
#         print("This email is already in dictionary!\n")
#     except NamesEmailError:
#         print("Name and email are already in dictionary!\n")


with open("data.json", "r") as json_file:
    data_ = json.load(json_file)
print(json.dumps(data_, indent=4, ensure_ascii=False))
