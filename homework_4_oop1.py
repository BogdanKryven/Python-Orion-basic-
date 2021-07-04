# 1. Create a Vehicle class with max_speed and mileage instance attributes
print("1. Create a Vehicle class with max_speed and mileage instance attributes")


class Vehicle:
    def __init__(self, max_speed, mileage_instance):
        self.max_speed = max_speed
        self.mileage_instance = mileage_instance


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have
# seating_capacity own method
print("""2. Create a child class Bus that will inherit all of the variables 
and methods of the Vehicle class and will have seating_capacity own method 
""")


class Bus(Vehicle):
    def __init__(self, seating_capacity, max_speed, mileage_instance):
        super().__init__(max_speed, mileage_instance)
        self.seating_capacity = seating_capacity
