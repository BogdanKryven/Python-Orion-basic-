class WrongType(Exception):
    pass


def decorator(arg_1, arg_2, arg_3, arg_4):
    def decor(func):
        def wrap(a, b, c):
            try:
                if isinstance(a, arg_1) and isinstance(b, arg_2) and isinstance(c, arg_3) \
                        and isinstance(func(a, b, c), arg_4):
                    return func(a, b, c)
                else:
                    raise WrongType

            except WrongType:
                return "Wrong type. Rewrite please"
        return wrap

    return decor


@decorator(int, float, int, float)
def func_(a, b, c):
    return sum([a, b, c])


print(func_('ss', 1.2, 4))
