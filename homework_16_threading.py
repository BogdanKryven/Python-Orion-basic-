import threading
from threading import Thread
from math import sqrt


def decorator_thread(func):
    def wrapper(*args):
        process_1 = Thread(target=func,
                           args=args)
        process_2 = Thread(target=func,
                           args=args)
        processes = [process_1, process_2]
        for i in processes:
            i.start()
            print(threading.get_ident())
            i.join()
    return wrapper


@decorator_thread
def quadratic_equation(a, b, c) -> str:
    d = pow(b, 2) - 4 * a * c
    if d > 0:
        results = (-b - sqrt(d)) / 2 * a, (-b + sqrt(d)) / 2 * a
        return f"The roots of quadratic equation " \
               f"{a}x^2 {'+' if b > 0 else '-'} " \
               f"{b if b > 0 else -b}x {'+' if c > 0 else '-'} " \
               f"{c if c > 0 else -c} = {results}"
    elif d == 0:
        result = -b / 2 * a
        return f"The root quadratic equation " \
               f"{a}x^2 {'+' if b > 0 else '-'} " \
               f"{b if b > 0 else -b}x {'+' if c > 0 else '-'} " \
               f"{c if c > 0 else -c} = {result}"
    else:
        return "No roots in quadratic equation"


print(quadratic_equation(float(input("a = ")), float(input("b = ")), float(input("c = "))))

# def decorator_thread():
#     process_1 = Thread(target=quadratic_equation,
#                        args=(int(float(input("a = "))), int(float(input("b = "))), int(float(input("c = ")))))
#     process_2 = Thread(target=quadratic_equation,
#                        args=(int(float(input("a = "))), int(float(input("b = "))), int(float(input("c = ")))))
#     processes = [process_1, process_2]
#     for i in processes:
#         i.start()
#         print(threading.get_ident())
#         i.join()


# process_11 = Thread(target=quadratic_equation,
#                     args=(int(float(input("a = "))), int(float(input("b = "))), int(float(input("c = ")))))
# print(process_11)
# process_21 = Thread(target=quadratic_equation,
#                     args=(int(float(input("x = "))), int(float(input("y = "))), int(float(input("z = ")))))
# print(process_11)
# process_31 = Thread(target=quadratic_equation,
#                     args=(int(float(input("x = "))), int(float(input("y = "))), int(float(input("z = ")))))
# print(process_31)
