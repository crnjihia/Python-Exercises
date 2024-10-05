import json

def contains_complex(json_string):
    try:
        data = json.loads(json_string)
        return any(isinstance(value, complex) for value in data.values())
    except ValueError:
        return False

# Example usage
json_string = '{"name": "John", "age": 30, "complex_number": "3+4j"}'
print(contains_complex(json_string))
