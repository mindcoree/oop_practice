from abc import ABC, abstractmethod


def permission_required(role):
    def decorator(class_method):
        def wrapper(self,*args):
            if self.role != 'admin':
                raise PermissionError('Your role User')
            return class_method(self,*args)
        return wrapper
    return decorator


class Animal(ABC):
    def __init__(self,role):
        self.role = role


    @abstractmethod
    def make_sound(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Cat(Animal):
    def make_sound(self):
        return 'МЯУ!!!!!'

class Dog(Animal):
    def make_sound(self):
        return 'ГАВ!!!!!'

class Lion(Animal):
    @permission_required('admin')
    def make_sound(self):
        return 'Pphaaa'


dog = Dog('user')
cat = Cat('user')
set_animals = {Dog('user'),Cat('user'),Lion('admin')}
for animal in set_animals:
    print(f"\nanimal: {animal}, make sound: {animal.make_sound()}\n")
