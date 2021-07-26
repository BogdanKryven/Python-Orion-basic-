from unittest import TestCase
from user import User


class TestUser(TestCase):
    def setUp(self) -> None:
        print("setUp")
        self.user_1 = User("Vasya", "Ivanov", 23)

    def tearDown(self) -> None:
        print("tearDown")
        del self.user_1

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_001(self):
        print("test_001")
        self.user_1.set_full_name("Vasyilev Mykhailo")

        self.assertEqual(self.user_1.name, "Mykhailo")
        self.assertEqual(self.user_1.surname, "Vasyilev")

    def test_002(self):
        print("test_002")
        self.user_1.set_full_name("Vasyilev Mykhailo")

        self.assertEqual(self.user_1.name, "Mykhailo")
        self.assertEqual(self.user_1.surname, "Vasyilev")
