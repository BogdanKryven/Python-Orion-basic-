from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange, choice
import time


class Animal(ABC):

    def __init__(self, speed: int, power: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, victim, forest: Forest, iD):
        raise NotImplementedError


class Predator(Animal):

    def __init__(self, speed: int, power: int):
        super().__init__(power, speed)
        self.max_power = power
        self.current_power = power
        self.speed = speed

        self.max_power = self.current_power

    def eat(self, victim, forest: Forest, iD):
        self.iD = iD

        print(f"I'm predator {self.iD}. My power is {self.current_power}, and my speed is {self.speed}")
        print(f"My victim is "
              f"{'predator' if isinstance(forest.animals[victim], Predator) else 'herbivorous'} whose id is [{victim}] "
              f"with power {forest.animals[victim].current_power} "
              f"and speed {forest.animals[victim].speed}")
        if self.current_power < 1:
            print("I'm died of starvation\n")
            forest.remove_animal(self.iD)

        if forest.animals[victim] == forest.animals[iD] or isinstance(forest.animals[victim], Predator):
            print(f"Unfortunately I had an unsuccessful hunt.\n")
            if self.current_power < 1:
                print("I'm died of starvation\n")
                forest.remove_animal(self.iD)

        elif isinstance(forest.animals[victim], Herbivorous):
            if self.current_power <= forest.animals[victim].current_power or self.speed <= forest.animals[victim].speed:
                self.current_power -= round(self.max_power * 0.3, 1)
                self.current_power = round(self.current_power, 1)

                forest.animals[victim].current_power -= round(forest.animals[victim].max_power * 0.3, 1)
                forest.animals[victim].current_power = round(forest.animals[victim].current_power, 1)
                if self.current_power < 1:
                    forest.remove_animal(self.iD)
                    print("I could not catch up / defeat my victim! I'm died of starvation\n")
                else:
                    print(f"I could not catch up / defeat my victim! Now my power is {self.current_power}, "
                          f"and my speed is {self.speed}\n")

            elif self.current_power > forest.animals[victim].current_power \
                    and self.speed > forest.animals[victim].speed:
                self.current_power += round(self.max_power * 0.5, 1)
                if self.current_power > self.max_power:
                    self.current_power = self.max_power
                print(f"The hunt is a success! I regained my strength! Now my power is {self.current_power}, "
                      f"and my speed is {self.speed}\n")
                forest.remove_animal(victim)


class Herbivorous(Animal):

    def __init__(self, speed: int, power: int):
        super().__init__(power, speed)
        self.max_power = power
        self.current_power = power
        self.speed = speed

        self.max_power = self.current_power

    def eat(self, victim, forest: Forest, iD):
        self.iD = iD

        print(f"I'm herbivorous {self.iD}, my power is {self.current_power}")
        if self.current_power < 1:
            print("I'm died of starvation\n")
            forest.remove_animal(self.iD)
        else:
            self.current_power += round(self.max_power * 0.5, 1)
            if self.current_power > self.max_power:
                self.current_power = self.max_power
            print(f"Delicious juicy lawn. I have eaten. Now my power is {self.current_power}\n")


class Forest:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, id_animals, animal):
        self.id_animals = id_animals
        self.animals[id_animals] = animal

    def remove_animal(self, id_animals):
        del self.animals[id_animals]

    def random_choice(self):
        return choice(list(self.animals.keys()))

    def see_forest(self):
        for animal1 in forest1.animals:
            return (f"Id {animal1}, power: {self.animals[animal1].max_power}, "
                  f"speed: {self.animals[animal1].speed}, "
                  f"{'- Predator' if isinstance(self.animals[animal1], Predator) else '- Herbivorous'}")

    @staticmethod
    def any_predator_left():
        status = True
        for value in forest1.animals.values():
            if isinstance(value, Herbivorous) and not isinstance(value, Predator):
                status = False
                break
        return status

    @staticmethod
    def any_herbivorous_left():
        status = True
        for value in forest1.animals.values():
            if isinstance(value, Predator) and not isinstance(value, Herbivorous):
                status = False
                break
        return status

    def hunting(self):
        list_of_keys = list(self.animals.keys())
        for key in list_of_keys:
            try:
                self.animals[key].eat(self.random_choice(), self, key)
                time.sleep(1)
            except KeyError:
                continue


forest1 = Forest()
animals = (choice([Predator, Herbivorous])(randrange(25, 100), randrange(25, 100)) for i in range(50))

for iD in range(5):
    animal = next(animals)
    forest1.add_animal(iD, animal)
forest1.see_forest()
while True:
    if forest1.any_predator_left():
        print("There are only Predators left!")
        print("Game over")
        break
    elif forest1.any_herbivorous_left():
        print("There are only Herbivorous left!")
        print("Game over")
        break
    forest1.hunting()
forest1.see_forest()