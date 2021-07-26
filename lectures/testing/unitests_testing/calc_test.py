from unittest import TestCase

from calc import Calc


class TestSum(TestCase):
    """
    тестування функції суми в калькуляторі
    """

    def test_001(self):
        self.assertEqual(Calc.sum(1, 2), 3)
        self.assertEqual(Calc.sum(2, 2), 4)
        self.assertEqual(Calc.sum(-2, 2), 0)

    def test_002(self):
        self.assertIsInstance(Calc.sum(1, 2), int)
        self.assertIsInstance(Calc.sum(1, 2.0), float)
        self.assertIsInstance(Calc.sum(1.0, 2.0), float)
        self.assertIsInstance(Calc.sum(1.0, 2), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.sum("1", 2)


class TestDiv(TestCase):
    def test_101(self):
        with self.assertRaises(ZeroDivisionError):
            Calc.div(1, 0)
