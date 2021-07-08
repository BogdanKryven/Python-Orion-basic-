class Person:
    __slots__ = ('name', 'surname')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


anna = Person('Anna', 8.5)
print(anna.__slots__)
print(anna.surname)
# anna.test = 'abc'
