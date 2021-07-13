from abc import ABC, abstractmethod


class Person:

    @abstractmethod
    def name(self, name):
        pass

    def age(self, age):
        if age > 18:
            print(age)

    def surname(self):
        pass

class Animal(ABC):
    @abstractmethod
    def feed(self, feed_type, lion_type):
        raise NotImplementedError

    @abstractmethod
    def eat(self):
        pass


class Lion(Animal):
    def feed(self, feed_type, lion_type):
        print(f'Feeding: {feed_type}, {lion_type}')

    def eat(self):
        print('Lion eats')


class Panda(Animal):
    def feed(self, feed_type, panda_type):
        print(f'Feeding: {feed_type}, {panda_type}')

    def eat(self):
        print('Panda eats')

class Snake(Animal):
    pass

lion = Lion()
panda = Panda()
# snake = Snake()
animals = (lion, panda)

for animal in animals:
    animal.eat()



# animal = Animal()
# try:
#     animal = Animal()
# except TypeError as e:
#     print(e)

# lion = Lion()
#
# lion.eat()
# lion.feed('meat', 'angry')
