import logging
import time
from random import randrange


# TASK 1


# class Calc:
#     def __init__(self, first, operation, second):
#         self.first = first
#         self.operation = operation
#         self.second = second
#
#     def sum_of_numbers(self):
#         sum_of_numbers = self.first + self.second
#         return f"{self.first} + {self.second} = {sum_of_numbers}"
#
#     def difference_of_numbers(self):
#         difference_of_numbers = self.first - self.second
#         if self.second >= 0:
#             print(f" {self.first} - {self.second} = {difference_of_numbers}")
#         else:
#             return f" {self.first} + {self.second * -1} = {difference_of_numbers}"
#
#     def multiplication_of_numbers(self):
#         multiplication_of_numbers = self.first * self.second
#         return f"{self.first} * {self.second} = {multiplication_of_numbers}"
#
#     def division_of_numbers(self):
#         if (self.first % self.second) == 0:
#             division_of_numbers = self.first // self.second
#         else:
#             division_of_numbers = round((self.first / self.second), 2)
#         return f" {self.first} / {self.second} = {division_of_numbers}"
#
#     def pow(self):
#         pow_of_numbers = pow(self.first, self.second)
#         return f"The number {self.first} brought to the power of {self.second} = {pow_of_numbers} "
#
#     def sqrt(self):
#         sqrt_of_numbers = round(self.first ** (1 / self.second), 5)
#         return f"The {self.second}th root of the power {self.first} = {sqrt_of_numbers}"
#
#     def percentage_of_number(self):
#         percent = round(((self.first / self.second) * 100), 2)
#         return f"The percentage of number {self.first} to number {self.second} = {percent}%"
#
#
# log_template = "%(levelname)s: %(filename)s: %(asctime)s - %(message)s"
# logging.basicConfig(level=logging.INFO, filename="Calc.log", filemode="a", format=log_template)
#
# while True:
#
#     num = Calc(input("\nInput your first number: "), input("Your operation: "), input("Input your second "
#                                                                                       "number: "))
#
#     for _ in range(1):
#
#         try:
#             num.first = float(num.first)
#             num.second = float(num.second)
#
#             if num.operation == "+":
#                 print(num.sum_of_numbers())
#                 logging.info("operation [+]")
#
#             elif num.operation == "-":
#                 print(num.difference_of_numbers())
#                 logging.info("operation [-]")
#
#             elif num.operation == "*":
#                 print(num.multiplication_of_numbers())
#                 logging.info("operation [*]")
#
#             elif num.operation == "pow":
#                 print(num.pow())
#                 logging.info("operation [pow]")
#
#             try:
#                 if num.operation == "/":
#                     print(num.division_of_numbers())
#                     logging.info("operation [/]")
#
#                 elif num.operation == "sqrt":
#                     print(num.sqrt())
#                     logging.info("operation [sqrt]")
#
#                 elif num.operation == "%":
#                     print(num.percentage_of_number())
#                     logging.info("operation [%]")
#
#             except ZeroDivisionError:
#                 if num.operation == "/":
#                     print("You cannot divide by zero")
#                     logging.warning("trying to divide by 0")
#
#                 elif num.operation == "sqrt":
#                     print("Cannot calculate the root of a negative number")
#                     logging.warning("Trying to make a root of 0 degree")
#
#                 elif num.operation == "%":
#                     print("It is impossible to know the percentage of any number from the number 0")
#                     logging.warning("Trying to find out the percentage of a number from 0")
#
#         except ValueError:
#             print("You didn't enter numbers. Try again")
#             logging.error("Entered not numbers")


# TASK 2


class LowWater(Exception):
    pass


class EmptyWater(Exception):
    pass


class LowBattery(Exception):
    pass


class DischargedButtery(Exception):
    pass


class ThreeQuartersTrashCan(Exception):
    pass


class AlmostFullTrashCan(Exception):
    pass


class FullTrashCan(Exception):
    pass


class StopAll(Exception):
    pass


class RobotVacuumCleaner:
    def __init__(self, battery_charge, trash_can, water):
        self.battery_charge = battery_charge
        self.trash_can = trash_can
        self.water = water
        self.ENERGY_REDUCE = 5
        self.WATER_REDUCE = 5

    def move(self):
        self.battery_charge -= self.ENERGY_REDUCE
        print("MOVE")

        if self.water <= 0 and self.trash_can >= 100:
            raise StopAll

        elif self.battery_charge <= 0:
            self.battery_charge = 0
            raise DischargedButtery

        elif self.battery_charge <= 20:
            raise LowBattery

        if self.water > 0:
            self.wash()
        if self.trash_can < 100:
            self.vacuum_cleaner()

        time.sleep(1)
        print("\n")

    def wash(self):
        if self.water > 0:
            self.water -= self.WATER_REDUCE
            print("WASH")

        if 20 >= self.water > 0:
            raise LowWater

        elif self.water - self.WATER_REDUCE <= 0:
            self.water = 0
            raise EmptyWater

    def vacuum_cleaner(self):
        if self.trash_can <= 100:
            self.trash_can += randrange(0, 10)
            print("VACUUM CLEANING")

        if 75 <= self.trash_can < 90:
            raise ThreeQuartersTrashCan

        elif 90 <= self.trash_can < 100:
            raise AlmostFullTrashCan

        elif self.trash_can + randrange(0, 10) >= 100:
            self.trash_can = 100
            raise FullTrashCan


cleaning = RobotVacuumCleaner(randrange(0, 100), randrange(0, 100), randrange(0, 100))
# print(cleaning.battery_charge, cleaning.trash_can, cleaning.water)

while True:
    try:
        print(cleaning.battery_charge, cleaning.water, cleaning.trash_can)
        cleaning.move()
    except LowBattery:
        print("My power is less then 20%. Put me on charge")
        if cleaning.water > 0:
            try:
                cleaning.wash()
            except LowWater:
                print("My water reserve is less then 20%. Replenish water supplies")
            except EmptyWater:
                print("I stopped wash. NO WATER!. Replenish water supplies!!!")
        if cleaning.trash_can < 100:
            try:
                cleaning.vacuum_cleaner()
            except ThreeQuartersTrashCan:
                print("My trash can is 75% full\n")
            except AlmostFullTrashCan:
                print("Please empty the trash can. My trash can is 90% full\n")
            except FullTrashCan:
                print(f"The VACUUM CLEANER IS FULL !!. I stopped vacuum cleaning!\n")
        print("\n")
        time.sleep(1)
    except DischargedButtery:
        print("I stopped move. No power. Put me on charge\n")
        break
    # except (FullTrashCan and EmptyWater):
    #     print("I stopped cleaning. The TRASH CAN IS FULL and there is NO WATER")
    #     break
    except StopAll:
        print("I stopped cleaning. The TRASH CAN IS FULL and there is NO WATER")
        break

    except LowWater:
        print("My water reserve is less then 20%. Replenish water supplies")
        if cleaning.trash_can < 100:
            try:
                cleaning.vacuum_cleaner()
            except ThreeQuartersTrashCan:
                print("My trash can is 75% full\n")
            except AlmostFullTrashCan:
                print("Please empty the trash can. My trash can is 90% full\n")
            except FullTrashCan:
                print(f"The VACUUM CLEANER IS FULL !!. I stopped vacuum cleaning!\n")
        time.sleep(1)
        print("\n")
    except EmptyWater:
        print("I stopped wash. NO WATER!. Replenish water supplies!!!")
        if cleaning.trash_can < 100:
            try:
                cleaning.vacuum_cleaner()
            except ThreeQuartersTrashCan:
                print("My trash can is 75% full\n")
            except AlmostFullTrashCan:
                print("Please empty the trash can. My trash can is 90% full\n")
            except FullTrashCan:
                print(f"The VACUUM CLEANER IS FULL !!. I stopped vacuum cleaning!\n")
        time.sleep(1)
        print("\n")

    except ThreeQuartersTrashCan:
        print("My trash can is 75% full\n")
        time.sleep(1)
    except AlmostFullTrashCan:
        print("Please empty the trash can. My trash can is 90% full\n")
        time.sleep(1)
    except FullTrashCan:
        print(f"The VACUUM CLEANER IS FULL !!. I stopped vacuum cleaning!\n")
