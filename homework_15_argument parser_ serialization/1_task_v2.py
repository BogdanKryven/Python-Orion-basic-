import json
from json_exceptions import NamesEmailError, NamesError, EmailError


class UserDataJson:
    @staticmethod
    def data_name():
        names = []
        try:
            for name in json.load(open("data.json"))["info"]:
                names.append(name["name"])
                return names
        except json.decoder.JSONDecodeError:
            return []

    @staticmethod
    def data_email():
        emails = []
        try:
            for email in json.load(open("data.json"))["info"]:
                emails.append(email["email"])
                return emails
        except json.decoder.JSONDecodeError:
            return []

        return emails

    def add_info(self):
        try:
            data = json.load(open("data.json"))
        except json.decoder.JSONDecodeError:
            data = {"info": []}

        users = {
            "name": f"{input('Input your name: ')}",
            "email": f"{input('Input your email: ')}"
        }
        if users.get("name") in self.data_name() and users.get("email") in self.data_email():
            raise NamesEmailError
        elif users.get("name") in self.data_name():
            raise NamesError
        elif users.get("email") in self.data_email():
            raise EmailError
        else:
            data["info"].append(users)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


for _ in range(int(input(f"How many users you want to add? "))):
    try:
        UserDataJson().add_info()
    except NamesError:
        print("This name is already in dictionary!\n")
    except EmailError:
        print("This email is already in dictionary!\n")
    except NamesEmailError:
        print("Name and email are already in dictionary!\n")
