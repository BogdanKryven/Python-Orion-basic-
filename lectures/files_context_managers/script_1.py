

file = open(r"test.txt", "rt")

print(file.readline())
print(file.readline())

file.close()

file = open(r"test.txt", "wt")

file.write("new_test11")

file.close()

file = open(r"test.txt", "at")
file.write("new_test11")
file.close()


# file = open(r"test_1.txt", "x")
# file.write("new_test11")
# file.close()


file = open(r"test.txt", "r+")
print(file.readline())
file.write("new_test11")

file.close()


file = open(r"test.jpg", "rb")
data = file.read()
file.close()


file = open(r"../../../files_context_manager/test_copy.jpg", "wb")
file.write(data)
file.close()
