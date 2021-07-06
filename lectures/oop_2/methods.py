def static_method():
    return print(f'static method called')


class MyClass:
    def __init__(self, test):
        self.test = test

    def method(self):
        self.foo()
        return print(f'instance methods called: {self}')

    @classmethod
    def test(cls):
        return print(f'class methods called: {cls}')

    @staticmethod
    def foo():
        return print(f'static method called')

my_class = MyClass('test')
MyClass.test()

class MyClass_2:

    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass_2.TOTAL_OBJECTS = MyClass_2.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print(f'Total objects: {cls.TOTAL_OBJECTS}')

obj_1 = MyClass_2()
obj_2 = MyClass_2()
obj_3 = MyClass_2()

MyClass_2.total_objects()

my_class = MyClass('test')
my_class.method()

MyClass.test()
MyClass.foo()

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza ({self.ingredients})'

    @classmethod
    def margarita(cls, ingredient):
        s = ['mozzarella', 'tomatos'].append(ingredient)
        return cls(s)

    @classmethod
    def proshuto(cls):
        return cls(['cheese', 'mushrooms'])

# print(Pizza.proshuto())
print(Pizza.margarita('souce'))
p1 = Pizza(['cheese', 'tomatos'])
print(p1.margarita('s'))

# p2 = Pizza(['cheese', 'mushrooms'])
# p3 = Pizza(['mozzarella', 'tomatos'])
# print(p)
