from functools import reduce

sum_ex = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
print(sum_ex)

numbers = [1, 2, 3, 4, 5]


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


reduce(my_add, numbers)
