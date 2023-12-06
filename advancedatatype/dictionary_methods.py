cars = {
    'bmw': {
        'model': '550i',
        'year': '2023',
        'owner': {
            'name': 'AJ Blues'
        }
    },
    'honda': {
        'model': 'Civic',
        'year': '2022',
        'owner': {
            'name': 'AJ Blues'
        }
    }
}

print(cars.keys())
print(cars.values())
print(cars.items())

cars_copy = cars.copy()
print(cars_copy)
print(cars['bmw'].pop('model'))
print(cars)
