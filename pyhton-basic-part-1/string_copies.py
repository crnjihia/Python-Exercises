def string_copies(s, n):
    if len(s) < 2:
        return s * n
    return s[:2] * n

print(string_copies("hello", 3))
