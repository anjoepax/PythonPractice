"""
String formatting in Python
"""
city = "NYC"
event = "show"

print("Welcome to " + city + " and enjoy the " + event)
print(f"Welcome to {city} and enjoy the {event}")
print("Welcome to %s and enjoy the %s" % (city, event))

a = "one two three"
b = a.split()
print(b)
