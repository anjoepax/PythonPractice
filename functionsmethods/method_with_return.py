"""
Method with Return values in Python
"""


# def multiply_num(n1, n2):
#     """
#     Multiply two numbers
#     :param n1:
#     :param n2:
#     :return:
#     """
#     return n1 * n2
#
#
# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
# print("Total: " + str(multiply_num(num1, num2)))


def is_metro(city):
    cities = ['seattle', 'nyc', 'la']
    if city in cities:
        return True
    else:
        return False


print(is_metro("la".lower()))

