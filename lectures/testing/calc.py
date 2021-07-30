

class Calc:
    @staticmethod
    def sum(a, b) -> int:
        """ Шукає суму двох чисел

        >>> Calc.sum(3, 2)
        5

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """
        return a + b

    @staticmethod
    def minus(a, b):
        """ Шукає різницю двох чисел

        >>> Calc.minus(3, 2)
        1

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """
        return a - b

    @staticmethod
    def mul(a, b):
        """ Шукає добуток двох чисел

                >>> Calc.mul(3, 2)
                6

                :param a: Перше число
                :param b: Друге число
                :return: Результат
                """
        return a * b

    @staticmethod
    def div(a, b):
        """ Шукає частку двох чисел

                >>> Calc.div(3, 2)
                1.5

                :param a: Перше число
                :param b: Друге число
                :return: Результат
                """
        return a / b

    @staticmethod
    def pow(a, b):
        """ Піднімає печше число до степеня другого числа

                >>> Calc.pow(3, 2)
                9

                :param a: Перше число (яке підносимо до степеня)
                :param b: Друге число (степінь до якого ми підносимо це число)
                :return: Результат
                """
        return pow(a, b)

    @staticmethod
    def sqrt(a, b) -> float:
        """ Взяття з під кореня

                >>> Calc.sqrt(16, 4)
                2.0

                :param a: Перше число (яке під коренем)
                :param b: Друге число (корінь якого степеня)
                :return: Результат
                """
        return round(a ** (1 / b), 5)

    @staticmethod
    def percentage_of_number(a, b) -> float:
        """ Шукає суму двох чисел

                >>> Calc.percentage_of_number(3, 100)
                3.0

                :param a: Перше число (число, яке ми прирівнюємо до іншого числа)
                :param b: Друге число (від якого і шукаємо відсоток)
                :return: Результат
                """
        return round(((a / b) * 100), 2)
