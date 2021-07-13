from random import random
PROJECT = 'CURSOR'

def simple_generator(value):
    while value > 0:
        value -= 1
        yield value


def increase(value):
    i = 0
    while value > 0:
        i += random()
        value -= 1
        yield round(i, 2)


gen = increase(5)

# for i in gen:
#     print(i)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Initialize the list
my_list = [1, 3, 6, 10]
# square each term using list comprehension
list_ = [x ** 2 for x in my_list]
# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)
# print(list_)
# print(generator)
# for i in generator:
#     print(i)

GREETINGS = ['Hi', 'Hello', 'Hola', 'Привіт']

for greeting in GREETINGS:
    print(greeting)


def generator_example():
    for greeting in GREETINGS:
        yield greeting

# generator_example = (greeting for greeting in GREETINGS)

def custom_generator():
    yield GREETINGS[0]
    yield GREETINGS[1]
    yield GREETINGS[2]
    yield GREETINGS[3]


def check_generator_value(gen):
    try:
        while True:
            print(f'Next value from generator: {next(gen)}')
    except StopIteration:
        print('That was the last one in generator')

greetings_gen = generator_example()
# check_generator_value(greetings_gen)

lst = []
for i in greetings_gen:
    if i == 'Hello':
        lst.append(i)

print(lst)
# check_generator_value(greetings_gen)

# ge = (g for g in GREETINGS)
# check_generator_value(GREETINGS)