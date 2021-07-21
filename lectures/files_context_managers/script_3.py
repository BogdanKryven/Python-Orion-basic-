import datetime

date = datetime.datetime.now()

name = "Misha"

with open("test_1.txt", "r") as file:
    template = file.read()
    mail = template.format(name, date)

print(mail)




