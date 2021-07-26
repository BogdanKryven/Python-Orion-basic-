

class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def set_full_name(self, full_name):
        """
        :param full_name: arg like "Klimchuk Mykhailo"
        :return:
        """
        self.surname, self.name = full_name.split(" ")
