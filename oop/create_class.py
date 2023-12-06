"""
Create class in Python
"""


class Car(object):

    def __init__(self, make="Audi", model="67i"):
        self.__make = make
        self.__model = model

    def get_car_make(self):
        return self.__make

    def get_car_model(self):
        return self.__model

    def set_car_make(self, set_make):
        self.__make = set_make

    def set_car_model(self, set_model):
        self.__model = set_model

    def __set_gauge(self):
        print("Private method")

    def print_something_non_sense(self):
        self.__set_gauge()


honda = Car("Civic")
print(honda.get_car_make())
print(honda.get_car_model())

toyota = Car("Vios", "EE56")
print(toyota.get_car_make())
print(toyota.get_car_model())

kia = Car()
kia.set_car_make("Kia")
kia.set_car_model("Sorento")
print(kia.get_car_make())
print(kia.get_car_model())
kia.print_something_non_sense()

