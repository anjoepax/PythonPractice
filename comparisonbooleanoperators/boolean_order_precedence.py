"""
Order of precedence for Boolean Operators
"""

"""
1. not
2. and
3. or
"""
bool_output = True or not False and False
# True or True and False
# True or False
# True
print(bool_output)

bool_output2 = 10 == 10 or not 10 > 11 and 10 > 15
print(bool_output2)

bool_output3 = (10 == 10 or not 10 > 11) and 10 > 15
# True or True -> True and False --> False
print(bool_output3)
