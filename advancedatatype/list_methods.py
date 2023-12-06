"""
Different method for List data type
"""
cars = ['Honda', 'BMW', 'Audi']
length_cars = len(cars)
print(length_cars)

# Append to the last
print("*#" * 20)
cars.append("Benz")
print(cars)

# Insert with specific index
print("*#" * 20)
cars.insert(2, "Jeep")
print(cars)

# Find index of the particular item in the list
print("*#" * 20)
x = cars.index("Benz")
print(x)

# Remove item on the list starting on the end
print("*#" * 20)
y = cars.pop()
print(cars)

# Remove item on the specific item
print("*#" * 20)
cars.remove("Jeep")
print(cars)

# Slicing a list
slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

# Sorting list
cars.sort()
print(cars)

# Reversing a list
cars.reverse()
print(cars)

print("*#" * 20)
text = [1, 2, 3, 2, 1, 2]
c = text.count(2)
print(c)

print("*#" * 20)
# Reversing a list
reverse_list = ["AJ", "Blues", "Manigos"]
reverse_list.reverse()
c = reverse_list
c.sort()
print(reverse_list)
c.reverse()
print(c)
