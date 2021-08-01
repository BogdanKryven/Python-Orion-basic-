

def out_func(arg_1):
    print("out_func", arg_1)

    def in_func_3():
        pass

    def in_func():
        print("in_func", arg_1)
        in_func_3()

    return in_func


in_func_2 = out_func(123)
