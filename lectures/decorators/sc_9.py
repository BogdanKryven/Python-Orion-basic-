

class SortAlgs:
    def __init__(self):
        self.sort_alg_dict = {
            "bubble": SortAlgs.__bubble_sort,
            "sort_2": SortAlgs.__sort_2,
        }

    @staticmethod
    def __bubble_sort(list_):
        return sorted(list_)

    @staticmethod
    def __sort_2(list_):
        return sorted(list_)


class Decor(SortAlgs):
    def __init__(self, filter_types, sort_alg="default"):
        super(Decor, self).__init__()
        if sort_alg != "default" and sort_alg not in self.sort_alg_dict:
            raise Exception("sort alg is not exist")

        self.filter_types = filter_types
        self.sort_alg = sort_alg

    def __filter(self, list_):
        new_list = []
        for el in list_:
            if isinstance(el, self.filter_types):
                new_list.append(el)
        return new_list

    def __sort(self, list_):
        if self.sort_alg == "default":
            return sorted(list_)
        alg = self.sort_alg_dict.get(self.sort_alg, None)

        return alg(list_)

    def __call__(self, func_):
        def wrap(list_):
            list_ = self.__filter(list_)
            list_ = self.__sort(list_)
            return func_(list_)
        return wrap


@Decor((int, float), "bubble")
def func(list_):
    print(list_)
    return sum(list_)


func([2, 0.5, 1, None, 2.3, "sdfg", [1, 2]])

