"""
Object-oriented programming in Python
"""


class Car:
    age = 0

    def __init__(self, age=101):
        self.age = age

    def get_age(self):
        return self.age


car = Car()
print("Age is: " + str(car.get_age()))
print(type(car))
