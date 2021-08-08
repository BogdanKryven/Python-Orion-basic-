class WrongType(Exception):
    pass


class DecoratorTypeR:
    def __init__(self, arg_1, arg_2, arg_3, arg_4):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
        self.arg_4 = arg_4

    def __call__(self, func):
        def wrap(a, b, c):
            try:
                if isinstance(a, self.arg_1) and isinstance(b, self.arg_2) and isinstance(c, self.arg_3) \
                        and isinstance(func(a, b, c), self.arg_4):
                    return func(a, b, c)
                else:
                    raise WrongType

            except WrongType:
                return "Wrong type. Rewrite please"

        return wrap


@DecoratorTypeR(int, float, int, float)
def func_(a, b, c):
    return sum([a, b, c])


print(func_(7, 1.2, 4))
