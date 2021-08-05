

def decor(flag, flag_2):
    def decor_in(func):
        def wrap(*args, **kwargs):
            print("Start")
            result = func(*args, **kwargs)
            print("Finish")
            return result

        def wrap_2(*args, **kwargs):
            print("Start")
            result = func(*args, **kwargs)
            print("Finish")
            return result

        if flag_2 is True:
            return wrap
        else:
            return wrap_2

    def decor_in_2(func):
        def wrap(*args, **kwargs):
            print("Start")
            result = func(*args, **kwargs)
            print("Finish")
            return result
        return wrap

    if flag is True:
        return decor_in
    else:
        return decor_in_2


@decor(True, True)
def func():
    pass
