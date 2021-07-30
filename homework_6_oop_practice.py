from __future__ import annotations
from abc import abstractmethod
from random import randrange


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, fruit_pests, vegetable_pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.fruit_pests = fruit_pests
        self.vegetable_pests = vegetable_pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'I have such vegetables {len(self.vegetables)}')
        print(f'I have such fruits {len(self.fruits)}')
        print(f'I have such fruit pests {self.fruit_pests}')
        print(f'I have such vegetable pests {self.vegetable_pests}')
        print(f"I'm a gardener {self.gardener}!\n")


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3

    def is_not_ripe(self):
        return self.states == 2


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

    def is_not_ripe(self):
        return self.states == 2


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]

    def count_of_tomatoes(self):
        return len(self.tomatoes)

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def all_are_not_ripe(self):
        return all([apple.is_not_ripe() for apple in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class AppleTree:
    def __init__(self, apples):
        self.apples = [Apple('White', index) for index in range(0, apples)]

    def count_of_apples(self):
        return len(self.apples)

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def all_are_not_ripe(self):
        return all([apple.is_not_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants


    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    def check_states(self, pest: Pests):
        if pest.number_of_pests > 0:
            print(f"There are {pest.number_of_pests} pests! You need to handling!")
        else:
            print(f"Everything is fine with the garden! There are {pest.number_of_pests} pests!")

    def handling(self, pest: Pests):
        pest.number_of_pests = 0
        print(f'I killed all of pests! Number of pests: {pest.number_of_pests}')


class Pests:

    def __init__(self, type_of_pests, number_of_pests):
        self.type_of_pests = type_of_pests
        self.number_of_pests = number_of_pests

    def show_the_pests(self):
        return f"I'm a {self.type_of_pests} pest! We are {self.number_of_pests} pieces!"

    def eat_fruit(self, tree: AppleTree):
        if tree.all_are_ripe() or tree.all_are_not_ripe():
            for _ in range(self.number_of_pests):
                if len(tree.apples) >= 1:
                    tree.apples.pop()
            apples_left = len(tree.apples)
            if self.number_of_pests == 0:
                print(f"There are {apples_left} APPLES.")
            elif apples_left >= 1 and self.number_of_pests >= 1:
                print(f"There are left {apples_left} APPLES. You must kill all pests!")
            else:
                print(f"There are left 0 APPLES. The harvest is lost.")

    def eat_vegetables(self, bush: TomatoBush):
        if bush.all_are_ripe() or bush.all_are_not_ripe():
            for _ in range(self.number_of_pests):
                if len(bush.tomatoes) >= 1:
                    bush.tomatoes.pop()
            tomatoes_left = len(bush.tomatoes)
            if self.number_of_pests == 0:
                print(f"There are {tomatoes_left} TOMATOES.")
            elif tomatoes_left > 0 and self.number_of_pests >= 1:
                print(f"There are left {tomatoes_left} TOMATOES!. You must kill all pests!")
            else:
                print(f"There are left 0 TOMATOES. The harvest is lost.")


tomato_bush = TomatoBush(5)
apple_tree = AppleTree(8)
pests_fruit = Pests('worms', randrange(0, 5))
pests_vegetable = Pests('snails', randrange(0, 3))

print("Sum of apples =", apple_tree.count_of_apples())
print("Sum of tomatoes =", tomato_bush.count_of_tomatoes(), "\n")
# Сума всіх яблук і сума всіх помідорів (корзин яблук і помідорів)

print(pests_fruit.show_the_pests())
print(pests_vegetable.show_the_pests(), "\n")
# Кількість шкідників

John = Gardener('John', [tomato_bush, apple_tree])
garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, fruit_pests=pests_fruit.number_of_pests,
                vegetable_pests=pests_vegetable.number_of_pests, gardener=John.name)

garden.show_the_garden()
# Показ саду (скільки чого є)
John.work()
John.work()
print("\n")

John.check_states(pests_fruit)
John.check_states(pests_vegetable)
# Показує статус чи є шкідники чи їх немає. Видає повідомлення що все ок, чи треба провести чистку "handling"

pests_fruit.eat_fruit(apple_tree)
pests_fruit.eat_fruit(apple_tree)
# Шкідники їдять фрукти
pests_vegetable.eat_vegetables(tomato_bush)
pests_vegetable.eat_vegetables(tomato_bush)
# Шкідники їдять овочі

John.handling(pests_fruit)
John.handling(pests_vegetable)
# Джон вбиває негадяїв

John.check_states(pests_fruit)
John.check_states(pests_vegetable)

print("\n", pests_fruit.show_the_pests())
print("\n", pests_vegetable.show_the_pests())

# Показує нову кількість шкідників