from math import sqrt


def decorator_hypotenuse(function):
    def wrap(a, b):
        hypo = function(a, b)
        print(f"При катетах {a}, {b} гіпотенуза = {hypo}")
        return hypo
    return wrap


@decorator_hypotenuse
def triangle(a=0, b=0):
    hypotenuse = sqrt(pow(a, 2) + pow(b, 2))
    print(hypotenuse)
    return hypotenuse


triangle(2, 3)
