import time


def decor_time_check(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(time.time() - t1)
        return result
    return wrap


@decor_time_check
def func_1(a):
    time.sleep(a)


print(func_1.__name__)

# @decor_time_check
# def func_2():
#     time.sleep(2)

#
# func_1(1)
# func_2()


# def func(*args):
#     print(args)
#
# def func(**kwargs):
#     print(kwargs)

def func(a1, b2=2, *args, **kwargs):
    print(a1)
    print(b2)
    print(args)
    print(kwargs)

# func(1, 2, 3, 4, 5, a=4, b=2, c=6)
