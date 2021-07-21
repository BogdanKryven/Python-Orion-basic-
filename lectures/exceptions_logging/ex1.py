

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"

    def save(self):
        pass


class ChildException(MyException):
    pass


el = MyException("arrr")
print(str(el))
