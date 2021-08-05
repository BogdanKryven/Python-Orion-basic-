

def decor(func):
    def wrap(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("Finish")
        return result
    return wrap


def decor_2(msg):
    def decor_in(func):
        def wrap(*args, **kwargs):
            print("Start")
            print(msg)
            result = func(*args, **kwargs)
            print("Finish")
            return result
        return wrap
    return decor_in


@decor_2("Hello")
@decor
def func_1():
    pass
