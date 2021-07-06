class Car:
    def __init__(self, engine):
        self.engine = engine


class Engine:
    def __init__(self):
        pass


engine = Engine()
# car = Car(engine)  # If I destroy this Car instance,
# the Engine instance still exists
