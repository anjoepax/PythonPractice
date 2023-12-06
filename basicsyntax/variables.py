"""
table
Object reference count
"""


a = "nyc"
b = "nyc"

print(a)

a = 123

print(a)

c = "nyc"
d = c
print(d == c)
print(d is c)

