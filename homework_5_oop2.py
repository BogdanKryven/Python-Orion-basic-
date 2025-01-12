from dataclasses import dataclass
from collections import namedtuple


# 1.


class Laptop:
    def __init__(self):
        battery = Battery("Battery fot laptop")


class Battery:
    def __init__(self, info):
        self.info = info


asus = Laptop()


# 2.


class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string1 = GuitarString()
guitar = Guitar(guitar_string1)


# 3


class Calc:
    @staticmethod
    def add_nums(a=0, b=0, c=0) -> (int, float):
        return a + b + c


d = Calc.add_nums(3, 4.9)
print(d)
print(type(d))

# 4*.


class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)


# 5*.


class Concert:
    max_visitor_num = 0

    def __init__(self):
        self.count = 0

    @property
    def visitors_count(self):
        return self.count

    @visitors_count.setter
    def visitors_count(self, value):
        # self.count = Concert.max_visitor_num if value > Concert.max_visitor_num else value
        self.count = value if value <= Concert.max_visitor_num else Concert.max_visitor_num


Concert.max_visitor_num = 50
concert = Concert()
concert1 = Concert()

concert.visitors_count = 1000
concert1.visitors_count = 49
print(concert.visitors_count)
print(concert1.visitors_count)


# ----------------------------------------------------------------------------------------------------------

class ConcertV1:
    max_visitor_number = 0

    def __init__(self, visitor_count=0):
        self.visitor_count = visitor_count

    @property
    def visitor_count(self):
        return self._visitor_count

    @visitor_count.setter
    def visitor_count(self, value):
        self._visitor_count = value if value <= ConcertV1.max_visitor_number else ConcertV1.max_visitor_number


ConcertV1.max_visitor_number = 50
concert = ConcertV1()
concert.visitor_count = 1000

concert1 = ConcertV1(49)
print(concert.visitor_count)
print(concert1.visitor_count)

# 6.
@dataclass
class AddressBookDataClass:
    key: str
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass('1', 'Bob', "+1-032-246-1037", '555 Route VT 78 Swanton, VT 05488',
                                    'bobmarley1@gmail.com', 'March 27th 1998', 23)
print(address_book)

# 7. Create the same class (6) but using NamedTuple
AddressBookDataClass = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number0', 'address', 'email',
                                                           'birthday', 'age'])

address_book = AddressBookDataClass('2', 'Elvis', '+1-064-458-1574', '765 Route VT 123 Brenton, CA 07634',
                                    'elvispresley2@gmail.com', 'April 19th 1976', 45)

print(address_book.age)
print(address_book[5])


# 8.


class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBookDatsClass(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age}'

    def __repr__(self):
        return f'AddressBookDatsClass(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age}'


address_book_info = AddressBook('2', 'Elvis', '+1-064-458-1574', '765 Route VT 123 Brenton, CA 07634',
                                'elvispresley2@gmail.com', 'April 19th 1976', 45)

print(address_book_info)
print(address_book_info.__str__())
print(str(address_book_info))
print(address_book_info.__repr__())


# 9.


class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


d = Person()
setattr(d, 'age', 33)
print(getattr(d, 'age'))


# 10.


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


p = Student(1, 'Bohdan')
setattr(p, 'email', 'xxx@xxx.com')
print("My name is", getattr(p, 'name'), "and Its my email:", getattr(p, 'email'))


# 11*.


class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        fahrenheit = (self._temperature * 1.8) + 32
        return fahrenheit

    @temperature.setter
    def temperature(self, new):
        print(f'Converted celsius to fahrenheit: {new}')


temp_1 = Celsius(34)
print(temp_1.temperature)
