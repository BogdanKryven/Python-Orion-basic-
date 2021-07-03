# 1. Define the id of next variables:
print("1. Define the id of next variables:")
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print("Define the id of int_a =", id(int_a))
print("Define the id of str_b =", id(str_b))
print("Define the id of set_c =", id(set_c))
print("Define the id of lst_d =", id(lst_d))
print("Define the id of dict_e =", id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
print("\n\n2. Append 4 and 5 to the lst_d and define the id one more time.")
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print("""Define the id of dict_e one more time 
after appending 4 and 5=""", id(lst_d))

# 3. Define the type of each object from step 1.
print("\n\n3. Define the type of each object from step 1.")
print("Define the type of int_a =", type(int_a))
print("Define the type of str_b =", type(str_b))
print("Define the type of set_c =", type(set_c))
print("Define the type of lst_d =", type(lst_d))
print("Define the type of dict_e =", type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print("\n\n4*. Check the type of the objects by using isinstance.")

check_isinstance_1 = isinstance("Anna has ___ apples and ___ peaches.", (float, int, list, dict, tuple, set, bytes))
check_isinstance_2 = isinstance("Anna has ___ apples and ___ peaches.", str)
print("Checking the type of the objects by using isinstance. Attempt #1:", check_isinstance_1)
print("Checking the type of the objects by using isinstance. Attempt #2:", check_isinstance_2)

print("\nChecking the type of the objects by using isinstance. int_1 is integer?", isinstance(int_a, int))
print("Checking the type of the objects by using isinstance. str_b is str?", isinstance(str_b, str))
print("Checking the type of the objects by using isinstance. set_c is set?", isinstance(set_c, set))
print("Checking the type of the objects by using isinstance. lst_d is list?", isinstance(lst_d, list))
print("Checking the type of the objects by using isinstance. dict_e is dict?", isinstance(dict_e, dict))

# 5. With .format and curly braces {}
num_apples = 10
num_peaches = 15
print("\n\n5. With .format and curly braces {}")
print("Anna has {} apples and {} peaches.".format(10, 15))

# 6. By passing index numbers into the curly braces.
print("\n\n6. By passing index numbers into the curly braces.")
print("Anna has {0} apples and {1} peaches.".format(10, 15))

# 7. By using keyword arguments into the curly braces.
print("\n\n7. By using keyword arguments into the curly braces.")
print("Anna has {nm_apples} apples and {nm_peaches} peaches.".format(nm_apples=5, nm_peaches=2))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("\n\n8*. With indicators of field size (5 chars for the first and 3 for the second)")
print("Anna has {1: 5} apples and {0: 3} peaches".format(10, 15))

# 9. With f-strings and variables
print("\n\n9. With f-strings and variables")
print(f'Anna has {num_apples} apples and {num_peaches} peaches.')

# 10. With % operator
print("\n\n10. With % operator")
print("Anna has %s apples and %s peaches" % (num_apples, num_peaches))

# 11*. With variable substitutions by name (hint: by using dict)
print("\n\n11*. With variable substitutions by name (hint: by using dict)")
my_dict = {"n_a": num_apples, "n_p": num_peaches}
print("Anna has %(n_a)s and %(n_p)s peaches" % my_dict)

# 12. Convert (1) to list comprehension
print("\n\n12. Convert (1) to list comprehension")
my_list_0 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(my_list_0)

# 13. Convert (2) to regular for with if-else
print("\n\n13. Convert (2) to regular for with if-else")

my_list_1 = []
for num in range(10):
    if num % 2 == 0:
        my_list_1.append(num // 2)
    else:
        my_list_1.append(num * 10)
print(my_list_1)

# 14. Convert (3) to dict comprehension.
print("\n\n14. Convert (3) to dict comprehension.")
my_dict_0 = {num_0: num_0 ** 2 for num_0 in range(1, 11) if num_0 % 2 == 1}
print(my_dict_0)

# 15*. Convert (4) to dict comprehension.
print("\n\n15*. Convert (4) to dict comprehension.")
my_dict_1 = {num_1: num_1 ** 2 if num_1 % 2 == 1 else num_1 // 0.5 for num_1 in range(1, 11)}
print(my_dict_1)

# 16. Convert (5) to regular for with if.
print("\n\n16. Convert (5) to regular for with if.")
my_dict_2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        my_dict_2[x] = x ** 3
print(my_dict_2)

# 17*. Convert (6) to regular for with if-else.
print("\n\n17*. Convert (6) to regular for with if-else.")
my_dict_3 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        my_dict_3[x] = x ** 3
    else:
        my_dict_3[x] = x
print(my_dict_3)

# 18. Convert (7) to lambda function
print("\n\n18. Convert (7) to lambda function")
foo_lmb = lambda x, y: x if x < y else y
print(foo_lmb(7, 6))

# 19*. Convert (8) to regular function
print("\n\n19*. Convert (8) to regular function")


def foo(x, y, z):
    if y < x & x > z:
        return z
    else:
        return y


print(foo(11, 7, 9))

# 20. Sort lst_to_sort from min to max
print("\n\n20. Sort lst_to_sort from min to max")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print("\n\n21. Sort lst_to_sort from max to min")
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("\n\n22. Use map and lambda to update the lst_to_sort by multiply each element by 2")
updated_list = list(map(lambda a: a * 2, lst_to_sort))
print(updated_list)

# 23*. Raise each list number to the corresponding number on another list:
print("\n\n23*. Raise each list number to the corresponding number on another list:")
list_A = [2, 3, 4]
list_B = [5, 6, 7]

list_C = list(map(lambda x: x + 3, list_A))
print(list_C)

list_D = list(map(lambda x, y: x ** y, list_A, list_B))
print(list_D)

list_E = list(map(pow, list_A, list_B))
print(list_E)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
print("\n\n24. Use reduce and lambda to compute the numbers of a lst_to_sort.")
from functools import reduce

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sum_lst_to_sort = reduce(lambda x, y: x + y, lst_to_sort)
print(sum_lst_to_sort)

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("\n\n25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.")
sorted_lst_to_sort = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(sorted_lst_to_sort)

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print("""\n\n26. Considering the range of values: b = range(-10, 10), 
use the function filter to return only negative numbers.""")
b = range(-10, 10)
filtered_b = list(filter(lambda x: (x < 0), b))
print(filtered_b)

# 27*. Using the filter function, find the values that are common to the two lists:
print("\n\n27*. Using the filter function, find the values that are common to the two lists:")
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)
