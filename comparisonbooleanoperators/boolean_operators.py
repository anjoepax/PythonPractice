"""
Boolean operators in Python
"""

"""
AND -- Truth Table
True -- True = True
True -- False = False
False -- True = False
False -- False = False
"""
# and operator
boolean_one = 10 > 5 and 8 < 10
print(boolean_one)

"""
OR -- Truth Table
True -- True = True
True -- False = True
False -- True = True
False -- False = False
"""
# or operator
boolean_two = 8 > 10 or 8 > 5
print(boolean_two)


"""
NOT -- Truth Table
True -- False
False -- True
"""
# not operator
boolean_three = not False
print(boolean_three)

passed = True
if not passed:
    print("Student failed")
else:
    print("Student passed")

