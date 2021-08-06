
def decor(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrap


@decor(int, float, int, float)
def func_(a, b, c, d):
    return a, b, c, d


print(func_(1, 1.2, 4))