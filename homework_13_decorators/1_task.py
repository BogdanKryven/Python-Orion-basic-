from time import time


def decorator_time(function):
    def wrap(*args, **kwargs):
        time_point_1_before = time()
        result = function(*args, **kwargs)
        time_point_2_after = time()

        print(time_point_2_after - time_point_1_before)
        return result
    return wrap


@decorator_time
def save_data():
    count_of_data = int(float(input("Input count of your data: ")))
    data_list = []
    for _ in range(count_of_data):
        data = input("\nInput: ").split(" ")
        [data_list.append(i) for i in data]
    print(data_list)


save_data()
