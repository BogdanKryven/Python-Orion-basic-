
class Observer:
    def __init__(self, cb):
        self.cb = cb

    def update(self):
        self.cb()


class Notificator:
    def __init__(self, id_):
        self.id = id_
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


def cb_1():
    print("cb_1")


def cb_2():
    print("cb_2")


notificator = Notificator("11")

observer_1 = Observer(cb_1)
observer_2 = Observer(cb_2)
observer_3 = Observer(cb_1)

notificator.add_observer(observer_1)
notificator.add_observer(observer_2)
notificator.add_observer(observer_3)


notificator.notify()
