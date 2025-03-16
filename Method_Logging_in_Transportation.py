from abc import abstractmethod, ABC


def log_class_methods(cls):
    def make_wrapper(method,name):
        def wrapper(*args):
            print('Method called')
            return method(*args)
        return wrapper

    for name in list(cls.__dict__):
        if not name.startswith('__'):
            method = cls.__dict__[name]
            if callable(method):
                setattr(cls,name,make_wrapper(method,name))
    return cls


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


@log_class_methods
class Car(Vehicle):
    def move(self):
        print('Машина едет по дороге.')


@log_class_methods
class Bicycle(Vehicle):
    def move(self):
        print('Велосипед едет по тропинке.')


@log_class_methods
class Airplane(Vehicle):
    def move(self):
        print("Самолет едет по тропосфере.")



for vehicle in (Car(),Bicycle(),Airplane()):
    vehicle.move()
