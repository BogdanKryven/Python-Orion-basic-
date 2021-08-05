

def decor(func):
    def wrap(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("Finish")
        return result
    return wrap


class MyClass:
    def __init__(self, arg):
        self.arg = arg
        # self.logger = Logger()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __enter__(self):
        pass

    def __call__(self, func):
        def wrap(*args, **kwargs):
            print("Start")
            print(self.arg)
            self.sort()
            with self as file:
                pass

            result = func(*args, **kwargs)
            print("Finish")
            return result
        return wrap

    def sort(self):
        pass


@MyClass("Hello")
def func_1():
    print("func_1")
    pass

func_1()
