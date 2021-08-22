
def coroutine(func):
    def wrap(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


@coroutine
def func():
    arg = yield
    print(arg)
    n = 2
    arg = yield n
    print(arg)
    yield 1

#
# gen = func()
#
# a = gen.send(12)
# b = gen.send(123)
# print(a, b)


@coroutine
def amount_balance():
    total = 0
    while True:
        balance = yield total
        total += balance


# am_gen = amount_balance()
# list = [1, 12, -1, 10, -30, 40, -2, 123]
#
# for i in list:
#     amount_balance = am_gen.send(i)
#     print(amount_balance)

def subgen():
    yield 1
    yield 2
    yield 3


def gen(sb):
    # yield from [1, 2, 3, 4]
    yield from sb
    yield 22
    yield 33


sb = subgen()
g = gen(sb)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
