# Program to filter out only the even items from a list
old_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), old_list))
print(new_list)  
# [4, 6, 8, 12]