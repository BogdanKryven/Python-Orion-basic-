

def hyp(a: int, b: int) -> float:
    """ Шукає гіпотенузу по даних катетах
    >>> hyp(3, 4)
    5.0
    >>> hyp(6, 9) # doctest: +SKIP
    10.0

    Використовуючи формулу с ** 2 = а ** 2 + b ** 2
    :param a: катет 1, може бути тільки інтом
    :param b: катет 2, може бути тільки інтом
    :return: гіпотенуза, float
    """
    hyp = (a ** 2 + b ** 2) ** 0.5
    return hyp
