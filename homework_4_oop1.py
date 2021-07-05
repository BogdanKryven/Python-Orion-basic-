# 1. Create a Vehicle class with max_speed and mileage instance attributes
from _operator import add


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have
# seating_capacity own method


class Bus(Vehicle):
    def __init__(self, seating_capacity, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


# 3. Determine which class a given Bus object belongs to (Check type of an object)
print("Checking type of an object (class Buss):", type(Bus))
print(isinstance(Bus, type))

# 4. Determine if School_bus is also an instance of the Vehicle class
School_bus = Bus(40, 80, 75000)
print(isinstance(School_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods
# from School and Bus and will have its own - bus_school_color


class SchoolBus(Bus):
    pass

    def bus_school_color():
        print("I'm painted yellow!")


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have
# make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.


class Bear:
    def make_sound(self):
        print("I'm a bear!")


class Wolf:
    def make_sound(self):
        print("I'm a wolf!")


bear = Bear()
wolf = Wolf()

for animal in (bear, wolf):
    animal.make_sound()


# 8. Create class City with name, population instance attributes, return
# a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def city_size(self):
        if self.population > 1500:
            # return self.population
            # It's to 8 point
            return f"The population of the city {self.name} is {self.population}"
        else:
            return "Your city is too small"


lviv = City('Lviv', 720000)
kyiv = City('Kyiv', 2800000)
lysynychi = City('Lysynychi', 1200)

for city_population in (lviv, kyiv, lysynychi):
    print(city_population.city_size())


# 10*. Override magic method __add__() to perform the additional action as
# 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.


class AddMethod:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 or other.count > 10:
            return self.count * other.count
        else:
            return self.count + other.count


c1 = AddMethod(10)
c2 = AddMethod(11)
c3 = c1 + c2
print('Result =', c3)


# 11. The __call__ method enables Python programmers to write classes where the instances
# behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.


class CallSum:
    def __call__(self, a, b):
        result = a + b
        # return result
        return f"Result = {result}"


d = CallSum()
print(d(4, 1142))


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length
# of the cart list is non-zero.


class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        len_my_str = len(self.cart)
        return len_my_str > 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))
