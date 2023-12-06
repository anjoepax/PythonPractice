"""
Exercise Section 8
"""


class Fruit(object):

    def __init__(self):
        print("You just created the Fruit class instance...")

    def nutrition(self):
        print("This is the nutrition of the fruit class...")

    def fruit_shape(self):
        print("This is the fruit shape of the fruit class...")


class Banana(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("You just created the Banana fruit class...")

    def nutrition(self):
        super(Banana, self).nutrition()
        print("This is the nutrition of the banana class....")

    def color(self):
        print("This is the color of the banana class...")

    def print_something(self):
        super(Banana, self).fruit_shape()
        print("Testing")


b = Banana()
b.nutrition()
b.color()
b.print_something()
