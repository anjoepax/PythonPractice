"""
Nested dictionary
"""
employee = {
    "id_number": 1131017,
    "first_name": "AJ",
    "last_name": "Manigos",
    "position": "QA Automation Analyst",
    "dependents": {
        "wife": "Irene May Fabul",
        "mother": "Allen Manigos"
    },
    "number_of_children": 3,
    "cars": [
        "BMW",
        "Toyota",
        "Audi",
        "Mercedes Benz"
    ]
}

father = {"father": "Ignacio Manigos"}
employee["dependents"].update(father)
print(employee)
print(employee['dependents'].get("wife"))
print(employee['dependents'].get("father"))
print(employee["cars"])
print(len(employee["cars"]))

print("*$" * 20)
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
        'year': '2022'
    }
}

print(cars['bmw']['owner']['name'])
