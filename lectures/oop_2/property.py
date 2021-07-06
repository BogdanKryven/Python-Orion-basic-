class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        p = (5 + 7 + 10) / 2
        result = (p * (p - 5) * (p - 7) * (p - 10)) ** 0.5
        return f'{self.name} {self.surname} {result}'

    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')


anna = Person('Anna', 'Tech')
anna.name = 'Alice'
print(anna.full_name)
# anna.full_name = 'Rob Sqad'
print(anna.name)
def full_name():
    pass
full_name = property(fget=full_name, fset=full_name)