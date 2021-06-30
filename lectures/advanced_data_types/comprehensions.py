
lst = []
for number in range(10):
    lst.append(number)
print(lst)

lst_comp = [number for number in range(10)]
print(lst_comp)

lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
print(lst)
# [1, 9, 25, 49, 81]

lst_comp = [num ** 2 for num in range(10) if num % 2 == 1]
print(lst_comp)
# [1, 9, 25, 49, 81]

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num ** 3)
    else:
        lst.append(num * 10)
print(lst)

lst_comp = [num ** 3 if num % 2 == 0 else num * 10 for num in range(10)]
print(lst_comp)

lst = []
a = [(1, 2, 3), (4, 5, 6)]

for tup in a:
    for num in tup:
        lst.append(num)
print(lst)


list_comprehension = [num * 2 for tup in [(1, 2, 3), (4, 5, 6)] for num in tup]
print(list_comprehension)
# [1, 2, 3, 4, 5, 6]

dct = {}
for x in [1, 2, 3, 4, 5]:
    dct[x] = x ** 2
print(dct)

dc_basic = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print(dc_basic)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dc_with_if = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dc_with_if)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

dc_with_elif = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dc_with_elif)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}