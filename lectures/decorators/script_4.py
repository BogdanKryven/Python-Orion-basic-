import time


def filter_(*args):
    def decor(func):
        def wrap(list_):
            new_list = []
            for el in list_:
                if isinstance(el, args):
                    new_list.append(el)

            result = func(new_list)

            return result
        return wrap
    return decor


def decor_time_check(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(time.time() - t1)
        return result
    return wrap

def method_executor(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            pass

    return wrap

#
# decor = filter_(int, float)
# wrap = decor(sum_)
# result = wrap([1, 2, 3, 4])


@method_executor
@decor_time_check
@filter_(int, float)
def sum_(list_):
    time.sleep(1)
    return sum(list_)


# result = filter_(int, float)(sum_)([1, 2, 3])


@filter_(int)
def minus(list_):
    return -sum(list_)


# filter_(int)(minus)([1, 2, 3, 4, 1.2, "sd"])


print(sum_([1, 2, 3, 4, 1.2, "sd"]))
# print(minus([1, 2, 3, 4, 1.2, "sd"]))



