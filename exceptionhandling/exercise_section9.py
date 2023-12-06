"""
Exercise section 9
"""


def exception_handling_exercise(key):
    car = {"make": "Honda", "model": "Civic", "year": "1995"}
    try:
        print(car[key])
    except KeyError:
        print(f"{key} key is not existing on the Dictionary")
    finally:
        print("Finally block, cleaning up now...")


exception_handling_exercise('model')
