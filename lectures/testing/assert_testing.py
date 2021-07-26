

assert sum([1, 2, 3]) == 6, "test error"


def func(a):
    if a is True:
        return "Hello"
    else:
        return 'by'


assert func(True) == "Hello"
assert func(False) == "by"


def hyp(a, b):
    hyp = (a ** 2 + b ** 2) ** 0.5
    return hyp

try:
    assert hyp(3, 4) == 5
except AssertionError:
    logger.warning("test failed")
