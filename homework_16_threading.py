import threading
from math import sqrt
import logging
import time

format_ = "%(asctime)s : %(message)s"
logging.basicConfig(format=format_, level=logging.INFO)


def decorator_time(func):
    def wrapper(*args, **kwargs):
        bef = time.monotonic()
        func(*args, **kwargs)
        logging.info(f"Time required {args[0]} thread: {time.monotonic() - bef}")

    return wrapper


@decorator_time
def quadratic_equation(name_thread_, a, b, c):
    time.sleep(1)
    logging.info(f"Thread-{name_thread_} starting!")
    d = pow(b, 2) - 4 * a * c
    if d > 0:
        results = (-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
        logging.info(f"The roots of quadratic equation "
                     f"{a}x^2 {'+' if b > 0 else '-'} "
                     f"{b if b > 0 else -b}x {'+' if c > 0 else '-'} "
                     f"{c if c > 0 else -c} = {results}")
    elif d == 0:
        result = -b / 2 * a
        logging.info(f"The root quadratic equation "
                     f"{a}x^2 {'+' if b > 0 else '-'} "
                     f"{b if b > 0 else -b}x {'+' if c > 0 else '-'} "
                     f"{c if c > 0 else -c} = {result}")
    else:
        logging.info("No roots in quadratic equation")
    logging.info(f"Thread {name_thread_} finishing!")


first = threading.Thread(target=quadratic_equation,
                         args=(1, 1, 3, 4))
second = threading.Thread(target=quadratic_equation,
                          args=(2, 1, 7, 3))
tasks = [first, second]
for i in tasks:
    i.start()
    logging.info(f"Indent {i.name}: {threading.get_ident()}")
for i in tasks:
    i.join()
