def decorator_of_list(*args):
    def decorator(function):
        def wrap(list_):
            print("List of elements before: ", list_)
            new_list = []
            for i in list_:
                if isinstance(i, args):
                    new_list.append(i)
                else:
                    try:
                        new_list.append(float(i))
                    except ValueError:
                        continue

            return function(new_list)

        return wrap

    return decorator


@decorator_of_list(int, float)
def list_of_elements(lst):
    print("List of elements after: ", lst)
    print("Sum of numbers", round(sum(lst), 2))
    return round(sum(lst), 2)


list_of_el = [3, 5, "1.1", "1", 1, 9, "a", "f", 1, 3]
list_of_elements(list_of_el)

# @decorator_of_list
# def list_of_elements():
#     numbers_list = []
#     count_of_numbers = int(input("Input count of numbers: "))
#     [numbers_list.append(i) for i in range(count_of_numbers)]
#     return sum(numbers_list)