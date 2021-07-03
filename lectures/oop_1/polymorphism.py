from multiple_inheritance import Person

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a cat and my name is {self.name} and I am {self.age} years old.')

    def make_sound(self, sound=''):
        print(sound)
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a dog and my name is {self.name} and I am {self.age} years old.')

    def make_sound(self, sound=''):
        print(sound)
        print('Bark')


cat = Cat('Kitty', 3)
dog = Dog('Rex', 5)

for animal in (cat, dog):
    animal.make_sound('s')
    animal.info()
    animal.make_sound()


