import json

# Python object
python_object = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python object to JSON data
json_data = json.dumps(python_object)

print(json_data)
