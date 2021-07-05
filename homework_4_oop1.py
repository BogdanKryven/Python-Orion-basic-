# 1. Create a Vehicle class with max_speed and mileage instance attributes


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

