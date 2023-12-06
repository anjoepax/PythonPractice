"""
String methods - Part 1
"""

# Accessing characters in a string
first = "NYC"
second = first[0]
print(first)
print(second)
print(len(first))


"""
len() - length of the string
lower() - Convert the string to lowercase
upper() - Convert the string to uppercase
str() - Convert to string
"""
str_sample = "THis Is The Sample String!"
print(str_sample.lower())
print(str_sample.upper())
print(len(str_sample))
print(str(str_sample))


print(str_sample + " " + str(3))


"""
Concatenation of string
"""
str_first_string = "Hello! "
str_second_string = "AJ Blues"
print(str_first_string + str_second_string)
