def decor(func):
    def wrap(self, *args, **kwargs):
        print("Hello")
        return func(self, *args, **kwargs)

    return wrap


class MyClass:
    def __init__(self):
        pass

    def __decor(func):
        def wrap(self, *args, **kwargs):
            print("Hello")
            return func(self, *args, **kwargs)

        return wrap

    @__decor
    @decor
    def func(self):
        print("func")


a = MyClass()
a.func()