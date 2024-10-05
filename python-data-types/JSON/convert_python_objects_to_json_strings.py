import json

# Python objects
python_objects = [
    {"name": "John", "age": 30},
    {"name": "Anna", "age": 25},
    {"name": "Mike", "age": 35}
]

# Convert Python objects to JSON strings and print all values
for obj in python_objects:
    json_string = json.dumps(obj)
    print(json_string)
