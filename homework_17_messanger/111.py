import json

with open("data.json", "r") as json_data:
    data_ = json.load(json_data)

nicks_ = []
for i in data_["info"]:
    nicks_.append(value for value in i.values())

print(nicks_)
print(data_["info"])
