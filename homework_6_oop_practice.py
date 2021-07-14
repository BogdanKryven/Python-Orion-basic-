import random
from abc import abstractmethod


# from random import randrange


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
    def __init__(self, vegetables, fruits, pests, gardener):
        # як воно з'єднується з іншими класами?!?!?!?! тут ж інші атрибути. Як воно взагалі все з'єднується я не розумію
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'I have such vegetables {len(self.vegetables)}')
        print(f'I have such fruits {len(self.fruits)}')
        print(f'I have such pests {self.pests}')
        # чому в овочах і фруктах працює лен а в шкідниках ні?? як можна зробити так щоб умова виконувалась?
        print(f"I'm a gardener {self.gardener}!")
        # як тут вивести його ім'я ?


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

    def is_fruit(self):
        return self.states == 2 and self.states == 3


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

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    # def all_are_ripe(self):
    #   lst = []
    #   for tomato in self.tomatoes:
    #     ripe_state = tomato.is_ripe()
    #       lst.append(ripe_state)
    #   return all(lst)

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def tomato_losses(self):
        for tomato in self.tomatoes:
            tomato -= 1


class AppleTree:
    def __init__(self, apples):
        self.apples = [Apple('White', index) for index in range(0, apples - 1)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def type_of_apples(self):
        return self.type_of_apples()

    # def numbers_of_apples(self):
    #     return len(self.apples)


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants
        # self.pests = pests

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    @staticmethod
    def check_states(pest):
        if pest.number_of_pests > 0:
            print(f"There are {pest.number_of_pests} pests! You need to handling!")
        else:
            print(f"Everything is fine with the garden! There are {pest.number_of_pests} pests!")

    @staticmethod
    def handling(pest):
        pest.kill()


# то саме. як тут видалити тих жуків повністю?!?! маю ідею про використання атрибуту іншого класу. але шось не працює
# перевірив і воно працює тільки коли цей клас я описую після класу pests інакше толку ноль

class Pests:

    def __init__(self, type_of_pests, number_of_pests):
        self.type_of_pests = type_of_pests
        self.number_of_pests = number_of_pests
        self.pests = [index for index in range(number_of_pests - 1)]

    def show_the_pests(self):
        return f"I'm a {self.type_of_pests} pest! We are {self.number_of_pests} pieces!"

    # def eat_fruit(self, tree: AppleTree):
    #     for _ in range(self.number_of_pests):
    #         apple_id = random.randint(0, len(tree.apples) - 1)
    #         if tree.apples[apple_id].is_ripe() or tree.apples[apple_id].is_not_ripe():
    #             print(f"I'm eating apple!!!I'm eating apple!!! --> ")
    #             tree.apples.pop()

    # def eat_apples(self, tree: AppleTree):
    #     count_of_apples = 0
    #     for count_of_apples in tree.apples: f
    #         pass

    def kill(self):
        self.number_of_pests = 0
        print(f'I killed all of pests! Number of pests: {self.number_of_pests}')


tomato_bush = TomatoBush(0)
apple_tree = AppleTree(5)
pests = Pests('worms', 2)

print(pests.show_the_pests())
John = Gardener('John', [tomato_bush, apple_tree])
garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests.number_of_pests, gardener=John)
# Детальніше пояснити за "tomato_bush.tomatoes" як воно працює і за інші атрибути. ЗВІДКИ ТІ "apples" "tomatoes"????????

garden.show_the_garden()
John.check_states(pests)
John.handling(pests)
John.check_states(pests)
print(pests.show_the_pests())

# John.work()
# John.work()
# John.work()

# print(apple_tree.apples)
#
# for apple in apple_tree.apples:
#     print(apple.number_of_apples)
