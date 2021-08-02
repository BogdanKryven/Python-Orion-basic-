def decorator_of_numbers(function):
    def wrap():
        result = function()
        str_res = [str(i) for i in result]
        return str_res
    return wrap


@decorator_of_numbers
def numbers_():
    numbers_list = []
    count_of_numbers = int(input("Input count of numbers: "))
    [numbers_list.append(i) for i in range(count_of_numbers)]
    # print(numbers_list)
    return numbers_list


print(numbers_())
