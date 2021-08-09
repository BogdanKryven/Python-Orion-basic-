import sys, json

args = sys.argv
list_of_args = []
del args[0]
for arg in args:
    list_of_args.append(arg)

serialized_list = json.dumps(list_of_args)
file = open('parse.json', 'w')
file.write(serialized_list)
file.close()