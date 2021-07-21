class Calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum_of_numbers(self):
        sum_of_numbers = self.first + self.second
        return f"The sum of numbers {self.first} and {self.second} is {sum_of_numbers}"

    def difference_of_numbers(self):
        difference_of_numbers = self.first - self.second
        return f"The difference of numbers {self.first} and {self.second} is {difference_of_numbers}"

    def multiplication_of_numbers(self):
        multiplication_of_numbers = self.first * self.second
        return f"The multiplication of numbers {self.first} and {self.second} is {multiplication_of_numbers}"

    def division_of_numbers(self):
        return self.first // self.second

    def pow(self):
        return pow(self.first, self.second)

    def sqrt(self):
        sqrt_of_numbers = round(self.first ** (1 / self.second), 5)
        return f"The {self.second}th root of the power {self.first} is {sqrt_of_numbers}"

    def percentage_of_number(self):
        percent = round(((self.first / self.second) * 100), 2)
        return f"The percentage of number {self.first} to number {self.second} is {percent}"


while True:

    num = Calc(int(input("\nInput your first number: ")), int(input("Input your second number: ")))
    type_of_operations = input("Your operation:")

    for _ in range(1):
        if type_of_operations == "+":
            print(num.sum_of_numbers())

        if type_of_operations == "-":
            print(num.difference_of_numbers())

        elif type_of_operations == "*":
            print(num.multiplication_of_numbers())

        elif type_of_operations == "/":
            print(num.division_of_numbers())

        elif type_of_operations == "pow":
            print(num.pow())

        elif type_of_operations == "sqrt":
            print(num.sqrt())

        elif type_of_operations == "%":
            print(num.percentage_of_number())
