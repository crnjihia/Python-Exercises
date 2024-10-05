def unique_key_values(python_object):
    return list(set(python_object.values()))

# Example usage
python_object = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name2": "John"
}
print(unique_key_values(python_object))
