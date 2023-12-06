"""
Dictionary data type
Data type tp store more than one value in one variable name, in terms of key value pairs
"""
cars = {
    'maker': 'Honda',
    'model': 'Civic',
    'year': [
        '2016',
        '2017',
        '2023'
    ],
    'owner': "Ramesh"
}

# roll_no = [5, 10, 15, 20]
# names = ['Ramesh', 'Pavan', 'Umesh', 'Kumar']
#
#
# cars.popitem()

print(cars)
print(cars['model'])

print(cars.get("maker"))
print(cars.get('year'))

print("*#" * 20)
d = {}
d["one"] = 1
d["two"] = 2
print(d)
sum_total = d['one'] + d['two']
print(sum_total)
d['sum'] = d['one'] + d['two']
print(d)
