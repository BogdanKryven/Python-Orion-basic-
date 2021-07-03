class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print(f'My name: {self.name}\nMy surname: {self.surname}\nMy age: {self.age}')

    def eat(self):
        print('cooking')


class Animals:
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def learn(self):
        print(f'Animal type: {self.animal_type}')

    def eat(self):
        print('hunting')


class Centaur(Person, Animals):
    def __init__(self, name, surname, age, animal_type):
        Person.__init__(self, name, surname, age)
        Animals.__init__(self, animal_type)

    def eat(self):
        print('eat')

john = Centaur('John', 'Ters', 754, 'Horse')

john.eat()

print(Centaur.mro())

class A:
    pass
    def process(self):
        print('A process()')


class B:
    pass
    def process(self):
        print('B process()')


class C(A, B):
    pass
    def process(self):
        print('C process()')

class F:
    def process(self):
        print('F process()')


class D(C, F):
    pass



obj = D()
obj.process()
print(D.mro())
