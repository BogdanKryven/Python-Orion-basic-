a = 5 + 5
a = 'st'
print(dir(a))


class TriangleArea:
    def __call__(self, a, b, c):
        p = (a + b + c) / 2
        result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return result

class Example:
    pass

ex = Example()
print(ex)

area = TriangleArea()

print(area(5, 4, 3))
