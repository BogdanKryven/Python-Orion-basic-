class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

    def get_name(self):
        return self.name

    def _get_surname(self):
        return self._surname

    def __get_age(self):
        return self.__age

    def get_info(self):
        name = self.get_name()
        surname = self._get_surname()
        age = self.__get_age()
        return name, surname, age


Anna = Person('Anna', 'Leo', 25)

a, b, c = Anna.get_info()
print(a, b, c)

print(Anna.name)
print(Anna.get_info())
print(Anna.get_surname())
print(Anna.get_age())
