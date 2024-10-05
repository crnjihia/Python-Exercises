import json

# JSON data as a string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON data to Python object
python_object = json.loads(json_data)

print(python_object)
