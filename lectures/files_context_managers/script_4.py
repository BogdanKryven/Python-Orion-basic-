

class MyOpen:
    def __init__(self, path, access_attr="r"):
        self.file = open(path, access_attr)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if exc_type is None:
            self.file.close()
        elif exc_type is Exception:
            print("EXCEPTION")
            return True


with open("test_1.txt", "r") as file:
    print(file.read())


with MyOpen("test_1.txt", "r") as file:
    print(file.read())
    float("f")




