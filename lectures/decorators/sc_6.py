from functools import wraps


def decor(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        """
        wrap
        :param args:
        :param kwargs:
        :return:
        """
        print("Hello")
        return func(*args, **kwargs)
    # wrap.__name__ = func.__name__
    # wrap.__doc__ = func.__doc__
    return wrap


@decor
def func_1():
    """
    func_1
    :return:
    """
    pass


print(func_1.__name__)
print(func_1.__doc__)
