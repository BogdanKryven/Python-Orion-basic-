def sum_num(a, b):
    return a + b


sum_num_lmb = lambda a, b: a + b
b = sum_num(5, 6)

a = lambda x: x * x
print(type(a))
print(type(sum_num))

rand_list = {5, 7, 1, 3}
print(sorted(rand_list))
# [1, 3, 5, 7]

print(sorted(rand_list, reverse=True))
# [7, 5, 3, 1]