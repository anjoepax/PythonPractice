"""
More built-in functions in Python
max(): It takes any number of arguments and returns the largest one
min(): It takes any number of arguments and returns the smallest one.
abs(): It returns the absolute value of the number, that number's distance from 0/
It always returns a positive value, and it only takes a single number.
type(): It returns the type of the data it receives as an argument.
"""


def return_largest_num(*args):
    """
    max() function
    :param args:
    :return:
    """
    print(max(args))
    return max(args)


return_largest_num(-20, -1, 78, 101)


def return_smallest_num(*args):
    """
    .min() function
    :param args:
    :return:
    """
    print(min(args))


return_smallest_num(-20, -79, -100, 10)


def abs_function(a):
    """
    .abs() function
    :param a:
    :return:
    """
    print(abs(a))


abs_function(-20)
abs_function(20)

string_sample = str(type("Hello World"))
print(string_sample == "<class 'str'>")
print(type(99.43))
print(type(78))
print(type("Hello World"))
ls = ["Hello", "World"]
print(type(ls))
