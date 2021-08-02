

def out_func(arg_1):
    print("out_func", arg_1)

    def in_func_3():
        pass

    def in_func1():
        print("in_func1", arg_1)
        in_func_3()

    def in_func():
        print("in_func", arg_1)
        in_func_3()

    return in_func, in_func1()


in_func_2 = out_func(123)
# in_func_2
in_func_3 = out_func(1234)
# in_func_3()