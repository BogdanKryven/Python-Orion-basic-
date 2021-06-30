def foo(x):
    return x * 2


lst = [1, 2, 3]
new_lst1 = list(map(lambda x: x * 2, lst))
new_lst = list(map(foo, lst))
print(new_lst)
print(new_lst1)

from functools import reduce

numbers = [0, 1, 2, 3, 4]


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


reduce(my_add, numbers)
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10
