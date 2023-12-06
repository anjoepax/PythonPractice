"""
String methods - Part 2
"""

"""
Replace string
"""
str_to_be_replace = "1abc2abc3abc4abc"
str_new_string = str_to_be_replace.replace('abc', 'def')
print(str_new_string)
print(str_to_be_replace.replace('abc', 'ABC', 3))


"""
Sub-String method
"""
sub_string = str_to_be_replace[0:6]
print(sub_string)

print("************************************************")
str_another_sample = "ThisIsAnotherSampleString"
sub_string = str_another_sample[0:10:3]
print(sub_string)
