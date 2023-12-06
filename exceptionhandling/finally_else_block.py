"""
Finally and else block
"""


def exception_handling():
    try:
        a = 10
        b = 20
        c = 2

        d = (a + b) // c
        print(d)
    except ZeroDivisionError:
        print("You cannot divide a number to a 0")
        raise ArithmeticError("Please change the 0 to any even number :D")
    except TypeError:
        print("Type error of one of the numbers, please double check.")
    else:
        print("If no exception, it will execute...")
    finally:
        print("Regardless if no exception or with exception, I will execute....")


exception_handling()
