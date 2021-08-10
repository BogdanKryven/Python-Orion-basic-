from unittest import TestCase
from homework_11_testing_v1.homework_11_testing import Calc
from homework_11_testing_v1.homework_11_testing import SqrtException


class TestSum(TestCase):
    """
    тестування методу суми
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestSum_001 is OK")
        self.assertEqual(Calc.sum(1, 2), 3)
        self.assertEqual(Calc.sum(2, 2), 4)
        self.assertEqual(Calc.sum(-2, 2), 0)
        self.assertEqual(Calc.sum(1, 2.0), 3)
        self.assertEqual(Calc.sum(2.0, 2), 4)
        self.assertEqual(Calc.sum(-2.0, 2), 0)

    def test_002(self):
        print("TestSum_002 is OK")
        self.assertIsInstance(Calc.sum(1, 2), int)
        self.assertIsInstance(Calc.sum(1, 2.0), float)
        self.assertIsInstance(Calc.sum(1.0, 2.0), float)
        self.assertIsInstance(Calc.sum(1.0, 2), float)
        self.assertIsInstance(Calc.sum(2.34, 3), float)

    def test_003(self):
        print("TestSum_003 is OK")
        self.assertRaises(TypeError, Calc.sum([23], [3]))
        self.assertRaises(TypeError, Calc.sum("1", 2))
        self.assertRaises(TypeError, Calc.sum([23], {3}))
        self.assertRaises(TypeError, Calc.sum(23, "2+j"))
        self.assertRaises(TypeError, Calc.sum([23], 3))


class TestDiff(TestCase):
    """
    тестування методу віднімання
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestDiff_001 is OK")
        self.assertEqual(Calc.diff(1, 2), -1)
        self.assertEqual(Calc.diff(2, 2), 0)
        self.assertEqual(Calc.diff(-2, 2), -4)

    def test_002(self):
        print("TestDiff_002 is OK")
        self.assertIsInstance(Calc.diff(1, 2), int)
        self.assertIsInstance(Calc.diff(1, 2.0), float)
        self.assertIsInstance(Calc.diff(1.0, 2.0), float)
        self.assertIsInstance(Calc.diff(1.0, 2), float)
        self.assertIsInstance(Calc.diff(2.34, 3), float)

    def test_003(self):
        print("TestDiff_003 is OK")
        self.assertRaises(TypeError, Calc.diff([23], [3]))
        self.assertRaises(TypeError, Calc.diff("1", 2))
        self.assertRaises(TypeError, Calc.diff([23], {3}))
        self.assertRaises(TypeError, Calc.diff(23, "2+j"))
        self.assertRaises(TypeError, Calc.diff([23], 3))


class TestMul(TestCase):
    """
    тестування методу множення
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestMul_001 is OK")
        self.assertEqual(Calc.mul(1, 2), 2)
        self.assertEqual(Calc.mul(2, 2), 4)
        self.assertEqual(Calc.mul(-2, 2), -4)

    def test_002(self):
        print("TestMul_002 is OK")
        self.assertIsInstance(Calc.mul(1, 2), int)
        self.assertIsInstance(Calc.mul(1, 2.0), float)
        self.assertIsInstance(Calc.mul(1.0, 2.0), float)
        self.assertIsInstance(Calc.mul(1.0, 2), float)
        self.assertIsInstance(Calc.mul(2.34, 3), float)

    def test_003(self):
        print("TestMul_003 is OK")
        self.assertRaises(TypeError, Calc.mul([23], [3]))
        self.assertRaises(TypeError, Calc.mul("1", 2))
        self.assertRaises(TypeError, Calc.mul([23], {3}))
        self.assertRaises(TypeError, Calc.mul(23, "2+j"))
        self.assertRaises(TypeError, Calc.mul([23], 3))


class TestDiv(TestCase):
    """
    тестування методу ділення
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestDiv_001 is OK")
        self.assertEqual(Calc.div(4, 2), 2)
        self.assertEqual(Calc.div(8, 2), 4)
        self.assertEqual(Calc.div(-2, 2), -1)

    def test_002(self):
        print("TestDiv_002 is OK")
        self.assertIsInstance(Calc.div(1, 2), float)
        self.assertIsInstance(Calc.div(1, 2.0), float)
        self.assertIsInstance(Calc.div(1.0, 2.0), float)
        self.assertIsInstance(Calc.div(1.0, 2), float)
        self.assertIsInstance(Calc.div(2.34, 3), float)

    def test_003(self):
        print("TestDiv_003 is OK")
        with self.assertRaises(TypeError):
            Calc.div([23], [3])
            Calc.div([23], [3])
            Calc.div("1", 2)
            Calc.div([23], {3})
            Calc.div(23, "2+j")

    def test_004(self):
        print("TestDiv_004 is OK")
        with self.assertRaises(ZeroDivisionError):
            Calc.div(23, 0)


class TestPow(TestCase):
    """
    тестування методу піднесення в степінь
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestPow_001 is OK")
        self.assertEqual(Calc.pow(4, 2), 16)
        self.assertEqual(Calc.pow(8, 2), 64)
        self.assertEqual(Calc.pow(-2, 2), 4)
        self.assertEqual(Calc.pow(0, 3), 0)

    def test_002(self):
        print("TestPow_002 is OK")
        with self.assertRaises(TypeError):
            Calc.pow([23], [3])
            Calc.pow([23], [3])
            Calc.pow("1", 2)
            Calc.pow([23], {3})
            Calc.pow(23, "2+j")


class TestSqrt(TestCase):
    """
    тестування методу взяття з під кореня
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestSqrt_001 is OK")
        self.assertEqual(Calc.sqrt(4, 2), 2)
        self.assertEqual(Calc.sqrt(9, 2), 3)

    def test_002(self):
        print("TestSqrt_002 is OK")
        with self.assertRaises(TypeError):
            Calc.sqrt([23], [3])
            Calc.sqrt([23], [3])
            Calc.sqrt("1", 2)
            Calc.sqrt([23], {3})
            Calc.sqrt(23, "2+j")

    def test_003(self):
        print("TestSqrt_003 is OK")
        with self.assertRaises(ZeroDivisionError):
            Calc.sqrt(1, 0)

    def test_004(self):
        print("TestSqrt_004 is OK")
        with self.assertRaises(SqrtException):
            Calc.sqrt(-2, -1)


class TestPercentage(TestCase):
    """
    тестування методу знаходження відсотка від числа
    """

    def setUp(self) -> None:
        print("\nStart")

    def tearDown(self) -> None:
        print("End")

    def test_001(self):
        print("TestPercentage_001 is OK")
        self.assertEqual(Calc.percentage_of_number(4, 100), 4.0)
        self.assertEqual(Calc.percentage_of_number(4, 50), 8.0)

    def test_002(self):
        print("TestPercentage_002 is OK")
        with self.assertRaises(TypeError):
            Calc.percentage_of_number([23], [3])
            Calc.percentage_of_number([23], [3])
            Calc.percentage_of_number("1", 2)
            Calc.percentage_of_number([23], {3})
            Calc.percentage_of_number(23, "2+j")

    def test_003(self):
        print("TestPercentage_003 is OK")
        with self.assertRaises(ZeroDivisionError):
            Calc.percentage_of_number(1, 0)
