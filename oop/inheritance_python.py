"""
Inheritance in Python
"""
from sandbox.another_oop_class import ClassOne


class Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

    def _print_info(self):
        print("Make of the car " + self.make)
        print("Model of the car " + self.model)


class Ship(object):
    anchor = 5

    def _dock_ship(self):
        print("Ship was docked...")


class Honda(Car, Ship, ClassOne):

    def __init__(self, make="Honda", model="Civic"):
        super().__init__(make, model)

    def honda_start(self):
        self.start()

    def honda_stop(self):
        self.stop()

    def print_honda_car_info(self):
        self._print_info()

    def non_sense_method(self):
        self._dock_ship()

    def method_from_external_class(self):
        self.method1()
        self.method2()


A550 = Honda(model="CRV")
A550.honda_start()
A550.honda_stop()
A550.print_honda_car_info()
A550.non_sense_method()
A550.method_from_external_class()
