from unittest import TestCase
from vector import Vec3f


class TestVector3f(TestCase):
    def setUp(self) -> None:
        self.vector_1 = Vec3f(1, 1, 1)
        self.vector_2 = Vec3f(1, -1, 0)

    def test_001(self):
        self.assertIsInstance(self.vector_1.x, int)
        self.assertIsInstance(self.vector_1.y, int)
        self.assertIsInstance(self.vector_1.z, int)

    def test_002(self):
        vector_3 = self.vector_1 + self.vector_2
        self.assertIsInstance(vector_3, Vec3f)

    def test_003(self):
        mul = self.vector_1 * self.vector_2
        self.assertIsInstance(mul, int)
