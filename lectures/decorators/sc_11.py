import time


def decor_for_method(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        print(time.time() - t1)
        return res
    return wrap


def decor_methods(cls):
    class Wrap:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                attr = super().__getattribute__(item)
            except AttributeError:
                pass
            else:
                return attr

            attr = self._obj.__getattribute__(item)

            if isinstance(attr, type(self.__init__)):
                return decor_for_method(attr)
            else:
                return attr

    return Wrap


@decor_methods
class MyClass:
    def __init__(self, name):
        self.name = name

    def func_1(self):
        time.sleep(1)

    def func_2(self):
        time.sleep(2)

    def func_3(self):
        time.sleep(2)


a = MyClass("Misha")
a.func_1()
a.func_2()
a.func_3()

print(a.name)

