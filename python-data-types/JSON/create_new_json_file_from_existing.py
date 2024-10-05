import json

# Read existing JSON file
with open('existing_file.json', 'r') as file:
    data = json.load(file)

# Create a new JSON file from the existing data
with open('new_file.json', 'w') as new_file:
    json.dump(data, new_file)
