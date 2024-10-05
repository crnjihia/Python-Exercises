import json

# Python dictionary
python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary (sorted by key) to JSON data with indent level 4
json_data = json.dumps(python_dict, sort_keys=True, indent=4)

print(json_data)
