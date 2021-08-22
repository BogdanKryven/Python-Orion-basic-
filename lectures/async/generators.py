import time


def func_1():
    while True:
        time.sleep(1)
        print("func_1")
        yield


def func_2():
    while True:
        time.sleep(1)
        print("func_2")
        yield


def event_loop():
    gen_1 = func_1()
    gen_2 = func_2()
    queue = [gen_1, gen_2]

    while True:
        gen = queue.pop(0)
        next(gen)
        queue.append(gen)


if __name__ == '__main__':
    event_loop()