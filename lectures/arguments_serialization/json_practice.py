import json

users = [
    {"username": "@vinni_puch.puh", "first_name": "Lubomur", "last_name": "Luzhnuy"},
    {"username": "pyatachok.puh", "first_name": "Hello", "last_name": "Hello"},
]

users = json.dumps(users)
f = open("parse.json", "w")
f.write(users)
f.close()
f = open('parse.json', "r")
json_obj = f.readline()
f.close()
user_data = json.loads(json_obj)
for user in user_data:
    print(user['username'])