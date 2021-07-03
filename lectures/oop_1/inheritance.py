class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print(f'My name: {self.name}\nMy surname: {self.surname}\nMy age: {self.age}')


class Student(Person):
    def __init__(self, subject, name, surname, age):
        super().__init__(name, surname, age)
        self.subject = subject

    def learn(self):
        print(f'I am learning {self.subject}')



john = Person('John', 'Barbie', 32)
john.print_info()

mike = Student('Math', 'Mike', 'Torse', 20)
mike.print_info()
mike.learn()


check = isinstance(mike, Student)
check_sub = issubclass(Student, Person)
print(check)
print(check_sub)