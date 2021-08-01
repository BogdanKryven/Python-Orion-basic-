from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange, choice
from typing import Any, Dict
from uuid import uuid4
from time import sleep


class Animal(ABC):

    def __init__(self, speed: int, power: int):
        self.id = uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed

        self.max_power = self.current_power

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):

    def __init__(self, speed: int, power: int):
        super().__init__(power, speed)
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        pick = choice(list(forest.animals.values()))

        print(f"I'm predator \n[{self.id}]. \nMy power is {self.current_power}, and my speed is {self.speed}")
        print(f"My victim is "
              f"{'predator' if isinstance(pick, Predator) else 'herbivorous'} whose id is \n[{pick.id}]\n"
              f"with power {pick.current_power} "
              f"and speed {pick.speed}")
        if self.current_power < 1:
            print("I'm died of starvation\n")
            forest.remove_animal(self)

        if pick.id == self or isinstance(pick, Predator):
            print(f"Unfortunately I had an unsuccessful hunt.\n")
            if self.current_power < 1:
                print("I'm died of starvation\n")
                forest.remove_animal(self)

        elif isinstance(pick, Herbivorous):
            if self.current_power <= pick.current_power or self.speed <= pick.speed:
                self.current_power -= round(self.max_power * 0.3, 1)
                self.current_power = round(self.current_power, 1)

                pick.current_power -= round(pick.max_power * 0.3, 1)
                pick.current_power = round(pick.current_power, 1)
                if self.current_power < 1:
                    forest.remove_animal(self)
                    print("I could not catch up / defeat my victim! I'm died of starvation\n")
                else:
                    print(f"I could not catch up / defeat my victim! Now my power is {self.current_power}, "
                          f"and my speed is {self.speed}\n")

            elif self.current_power > pick.current_power \
                    and self.speed > pick.speed:
                self.current_power += round(self.max_power * 0.5, 1)
                if self.current_power > self.max_power:
                    self.current_power = self.max_power
                print(f"The hunt is a success! I regained my strength! Now my power is {self.current_power}, "
                      f"and my speed is {self.speed}\n")
                forest.remove_animal(pick)


class Herbivorous(Animal):

    def __init__(self, speed: int, power: int):
        super().__init__(power, speed)
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):

        print(f"I'm herbivorous \n[{self.id}], my power is {self.current_power}")
        if self.current_power < 1:
            print("I'm died of starvation\n")
            forest.remove_animal(self)
        else:
            self.current_power += round(self.max_power * 0.5, 1)
            if self.current_power > self.max_power:
                self.current_power = self.max_power
            print(f"Delicious juicy lawn. I have eaten. Now my power is {self.current_power}\n")


class Forest:

    def __init__(self):
        self.animals: Dict[str, Any[Predator, Herbivorous]] = dict()

    def add_animal(self, animal_: Any[Predator, Herbivorous]):
        self.animals[animal_.id] = animal_

    def remove_animal(self, animal_: Any[Predator, Herbivorous]):
        del self.animals[animal_.id]

    def random_choice(self):
        return choice(list(self.animals.keys()))

    def see_forest(self):
        for animal_ in self.animals:
            print(f"Id [{self.animals[animal_].id}], power: {self.animals[animal_].max_power}, "
                  f"speed: {self.animals[animal_].speed}, "
                  f"{'- Predator' if isinstance(self.animals[animal_], Predator) else '- Herbivorous'}")

    def any_predator_left(self):
        return any(isinstance(value, Predator) for value in self.animals.values())

    def any_herbivorous_left(self):
        return any(isinstance(value, Herbivorous) for value in self.animals.values())


def animal_generator():
    animals = choice([Predator, Herbivorous])
    current_power = randrange(25, 100)
    speed = randrange(25, 100)
    animals_ = animals(speed=speed, power=current_power)

    return animals_


if __name__ == "__main__":
    COUNT_OF_ANIMALS = int(input("Input number of animals: "))
    forest_ = Forest()

    for _ in range(COUNT_OF_ANIMALS):
        animal = animal_generator()
        forest_.add_animal(animal)
    forest_.see_forest()
    print('\n')

    while True:
        if not forest_.any_herbivorous_left():
            print("There are only Predators left!")
            print("Game over")
            break
        elif not forest_.any_predator_left():
            print("There are only Herbivorous left!")
            print("Game over")
            break
        for _ in list(forest_.animals.values()):
            animal = choice(list(forest_.animals.values()))
            animal.eat(forest=forest_)
            sleep(1)

    forest_.see_forest()
