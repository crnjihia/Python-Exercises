import json

# JSON encoded data as a string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON encoded data to Python objects
python_object = json.loads(json_data)

print(python_object)
