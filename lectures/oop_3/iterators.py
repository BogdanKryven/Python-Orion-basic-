lst = [0, 1, 2, 3]
# for x in lst[::-1]:
#     print(x)

iter_lst = iter(lst[::-1])
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))


# lst = ['Anna', 'Vasyl', 'Andriy']
# dct = {1: 'one', 2: 'two', 3: 'three'}
# iter_dct = iter(dct)
# print(iter_dct)
# iter_lst = iter(lst)
# for i in iter_dct:
#     print(i)

# print(next(iter_dct))
# print(next(iter_dct))
# print(next(iter_dct))
# print(next(iter_dct))

# name = next(iter_lst)
# print(name)
#
# ###
# ###
# ###
# name = next(iter_lst)
# print(name)
#
# ####
# ####
# ###
# name = next(iter_lst)
# print()

def check_if_object_is_iterable(obj):
    return '__getitem__' in dir(obj)


types_to_check = [int, bool, str, list, tuple, set, dict, frozenset, float, complex, bytes, bytearray]
for step_type in types_to_check:
    print(f'{step_type} Iterable {check_if_object_is_iterable(step_type)}')
