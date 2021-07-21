import pickle

list_1 = [1, 2, 3, 4, 5]

# data = pickle.dumps(list_1)
#
# obj = pickle.loads(data)
# print(type(obj))
# print(obj)

file = open("../../../files_context_manager/list", "rb")
obj = pickle.load(file)
print(type(obj))
print(obj)
file.close()
