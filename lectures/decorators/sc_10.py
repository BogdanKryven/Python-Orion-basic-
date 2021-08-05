

def decor(filter_types, sort_alg="default"):
    def decor_in(func_):
        def wrap(list_):
            def __filter(list_int_filter):
                new_list = []
                for el in list_int_filter:
                    if isinstance(el, filter_types):
                        new_list.append(el)
                return new_list

            def __sort(list_):
                def __bubble_sort(list_):
                    return sorted(list_)

                def __sort_2(list_):
                    return sorted(list_)

                if sort_alg == "default":
                    return sorted(list_)
                elif sort_alg == "bubble":
                    return __bubble_sort(list_)
                elif sort_alg == "sort_2":
                    return __sort_2(list_)
                else:
                    raise Exception("sort alg is not exist")

            list_ = __filter(list_)
            list_ = __sort(list_)
            return func_(list_)
        return wrap
    return decor_in


@decor((int, float), "bubble")
def func(list_):
    print(list_)
    return sum(list_)


func([2, 0.5, 1, None, 2.3, "sdfg", [1, 2]])
