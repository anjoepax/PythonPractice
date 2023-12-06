"""
Modules in python
"""
from math import sqrt
# from modules import create_own_modules as car
from modules.create_own_modules import info


class ModulesDemo(object):

    def builtin_modules(self):
        print(sqrt(100))

    def car_description(self):
        make = 'BMW'
        model = '550i'
        info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_description()
