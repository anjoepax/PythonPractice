"""
Positional and Optional Parameters
"""


def sum_nums(n1=2, n2=4):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(2, 8)
sum2 = sum_nums(5, 3)
sum3 = sum_nums()
print(sum1)
print(sum2)
print(sum3)


# Positional Parameters
sum4 = sum_nums(n2=78, n1=56)
print(sum4)

