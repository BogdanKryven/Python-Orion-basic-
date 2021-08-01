
def decor(func_):
    def wrap(n):
        result = func_(n)
        print("wrap", result)
        new_list = [str(el) for el in result]
        return new_list
    return wrap


@decor
def func(n):
    return [i for i in range(n)]


# print(func(10))


def wrap_func():
    list_ = func(10)
    new_list = [str(el) for el in list_]
    return new_list


def sign_decor(func):
    def wrap():
        msg = func()
        msg += "\nMisha"
        return msg
    return wrap


@sign_decor
def get_msg():
    return "MSG MSG MSG MSG MSG MSG MSG"

print(get_msg())