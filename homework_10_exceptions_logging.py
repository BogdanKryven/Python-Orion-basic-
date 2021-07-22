import logging


class Calc:
    def __init__(self, first, operation, second):
        self.first = first
        self.operation = operation
        self.second = second

    def sum_of_numbers(self):
        sum_of_numbers = self.first + self.second
        return f"{self.first} + {self.second} = {sum_of_numbers}"

    def difference_of_numbers(self):
        difference_of_numbers = self.first - self.second
        if self.second >= 0:
            print(f" {self.first} - {self.second} = {difference_of_numbers}")
        else:
            return f" {self.first} + {self.second * -1} = {difference_of_numbers}"

    def multiplication_of_numbers(self):
        multiplication_of_numbers = self.first * self.second
        return f"{self.first} * {self.second} = {multiplication_of_numbers}"

    def division_of_numbers(self):
        if (self.first % self.second) == 0:
            division_of_numbers = self.first // self.second
        else:
            division_of_numbers = round((self.first / self.second), 2)
        return f" {self.first} / {self.second} = {division_of_numbers}"

    def pow(self):
        pow_of_numbers = pow(self.first, self.second)
        return f"The number {self.first} brought to the power of {self.second} = {pow_of_numbers} "

    def sqrt(self):
        sqrt_of_numbers = round(self.first ** (1 / self.second), 5)
        return f"The {self.second}th root of the power {self.first} = {sqrt_of_numbers}"

    def percentage_of_number(self):
        percent = round(((self.first / self.second) * 100), 2)
        return f"The percentage of number {self.first} to number {self.second} = {percent}%"


while True:

    num = Calc(input("\nInput your first number: "), input("Your operation: "), input("Input your second "
                                                                                      "number: "))

    for _ in range(1):

        try:
            num.first = float(num.first)
            num.second = float(num.second)
            if num.operation == "+":
                print(num.sum_of_numbers())

            elif num.operation == "-":
                print(num.difference_of_numbers())

            elif num.operation == "*":
                print(num.multiplication_of_numbers())

            elif num.operation == "/":
                try:
                    print(num.division_of_numbers())
                except ZeroDivisionError:
                    print("You cannot divide by zero")

            elif num.operation == "pow":
                print(num.pow())

            elif num.operation == "sqrt":
                try:
                    print(num.sqrt())
                except TypeError:
                    print("Cannot calculate the root of a negative number")

            elif num.operation == "%":
                print(num.percentage_of_number())

        except ValueError:
            print("You didn't enter numbers. Try again")
