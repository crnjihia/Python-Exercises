def add_if_integers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return "Both inputs must be integers."

print(add_if_integers(5, 10))
