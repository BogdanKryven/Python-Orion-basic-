from abc import abstractmethod
# from random import randrange
import random



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
        self.apples = [Apple('White', index) for index in range(0, apples)]
        # self.sum_of_apples = len(self.apples)

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

    def type_of_apples(self):
        return self.type_of_apples()

    # @property
    # def sum_of_apples(self, pest: Pests):
    #     count_apples = 0
    #     for apple in self.apples:
    #         count_apples += apple.number_of_apples
    #     if self.all_are_ripe() or self.all_are_not_ripe():
    #         count_apples = self.sum_of_apples - pest.number_of_pests
    #     return count_apples

    # @sum_of_apples.setter
    # def sum_of_apples(self, value):
    #     if self.all_are_ripe() or self.all_are_not_ripe():
    #         self.sum_of_apples = self.sum_of_apples - Pests.count_of_pests
    #         self.sum_of_apples = value


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
    #     if tree.all_are_ripe() or tree.all_are_not_ripe():
    #         tree.apples_left = tree.sum_of_apples() - self.number_of_pests
    #         print(f"I ate {self.number_of_pests} apples! {tree.apples_left} apples left")
    #     return tree.apples_left

    # def eat_fruit(self, tree: AppleTree):
    #     if tree.all_are_ripe() or tree.all_are_not_ripe():
    #         tree.apples_left = tree.sum_of_apples - self.number_of_pests
    #         print(f"I ate {self.number_of_pests} apples! {tree.apples_left} apples left")
    #     return tree.apples_left

    # def eat_fruit(self, tree: AppleTree):
    #     for _ in tree.apples:
    #         for pest in range(0, self.number_of_pests - 1):
    #             tree.apples.pop()

    def eat_fruit(self, tree: AppleTree):
        if tree.all_are_ripe() or tree.all_are_not_ripe():
            for _ in range(self.number_of_pests):
                if len(tree.apples) >= 1:
                    tree.apples.pop()
            apples_left = len(tree.apples)
            if apples_left >= 0:
                print(f"There are left {apples_left} apples")
            else:
                print(f"There are left 0 apples")

    def kill(self):
        self.number_of_pests = 0
        print(f'I killed all of pests! Number of pests: {self.number_of_pests}')

    def count_of_pests(self):
        return self.number_of_pests


tomato_bush = TomatoBush(0)
apple_tree = AppleTree(15)
pests = Pests('worms', randint(0, 5))
# print("Sum of apples = ", apple_tree.sum_of_apples)
# Сума всіх яблук

print("\n", pests.show_the_pests())
# Кількість шкідників

John = Gardener('John', [tomato_bush, apple_tree])
garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests.number_of_pests,
                gardener=John.name)
# Детальніше пояснити за "tomato_bush.tomatoes" як воно працює і за інші атрибути. ЗВІДКИ ТІ "apples" "tomatoes"????????

garden.show_the_garden()
# Показ саду (скільки чого є)
John.work()
John.work()

John.check_states(pests)
# Показує статус чи є шкідники чи їх немає. Видає повідомлення що все ок, чи треба провести чистку "handling"
# pests.eat_fruit(apple_tree)
#
# pests.eat_fruit(apple_tree)
# Шкідники їдять фрукти

# print("\n", John.handling(pests))
# John.handling(pests)
# Джон вбиває негадяїв
John.check_states(pests)
print("\n", pests.show_the_pests())
# Показує нову кількість шкідників

# pests.eat_fruit(apple_tree)
# print(apple_tree.summa_of_apples)

print(type(pests.count_of_pests()))

# print(len(apple_tree.apples))
# print(pests.number_of_pests)

pests.eat_fruit(apple_tree)
pests.eat_fruit(apple_tree)
pests.eat_fruit(apple_tree)
pests.eat_fruit(apple_tree)
pests.eat_fruit(apple_tree)


print(apple_tree.count_of_apples())













