

class Vec3f:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: int):
        self.x += other
        self.y += other
        self.z += other
        return self

    def __mul__(self, other: int):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __save(self):
        self.x = self.__temp_vector.x
        self.y = self.__temp_vector.y
        self.z = self.__temp_vector.z
        self.__temp_vector = None

    def __str__(self):
        return f"({self.x}; {self.y}; {self.z})"

    def __enter__(self):
        self.__temp_vector = Vec3f(self.x, self.y, self.z)
        return self.__temp_vector

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__save()
        elif exc_type is TypeError:
            self.__temp_vector = None
            return True
        else:
            self.__temp_vector = None
            return False


vec_1 = Vec3f(1, 2, 3)
with vec_1 as vec:
    vec += 1
    vec *= 10
    # print(vec)
    # vec += "1"
    raise ZeroDivisionError

print(vec_1)

