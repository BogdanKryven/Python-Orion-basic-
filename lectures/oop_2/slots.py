class Person:
    __slots__ = ('name', 'surname')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


anna = Person('Anna', 'Tech')
print(anna.__slots__)
print(anna.name)
# anna.test = 'abc'
