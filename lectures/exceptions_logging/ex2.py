#
# a = "3"
# b = 1
# try:
#     try:
#         c = a / b
#     except ZeroDivisionError:
#         c = 0
#     except (TypeError, ValueError) as ex:
#         print("a or b is not number")
#         raise ex
#     except Exception:
#         print("Exception")
#     else:
#         print("else")
#     finally:
#         print("finally")
# except TypeError:
#     print("Type error except")
#
# if b == 0:
#
#     c = 0
#
# # print("c:", c)
# print("end")


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
#
# try:
#     # raise Exception(1, 2, 3,"123",4 ,5 ,)
#     a = int("qwe")
# except Exception as ex:
#     print(ex.args)
#


class MyException1(Exception):
    pass


def func():
    f = 0
    a = 0
    while True:
        f += 1
        a += 1
        if f == 10:
            raise MyException()
        if a == 5:
            raise MyException1()


try:
    func()
except MyException:
    print("func finish")
except MyException1:
    print("func finish")
