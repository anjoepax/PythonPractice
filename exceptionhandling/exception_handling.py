"""
Exceptions are errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
"""


def exception_handling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) // c
        print(d)
    except ZeroDivisionError:
        print("You cannot divide a number to a 0")
    except TypeError:
        print("Type error of one of the numbers, please double check.")


exception_handling()
