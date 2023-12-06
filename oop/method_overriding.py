"""
Method overriding in Python
"""


class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def driver(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")


class BMW(Car):

    def __init__(self):
        super().__init__()
        print("You just created the BMW instance")

    def driver(self):
        print("You are driving a BMW, enjoy!!!")

    def headsup_display(self):
        super(BMW, self).driver()
        print("This is a unique feature...")


car = BMW()
car.driver()
car.headsup_display()
car.stop()

