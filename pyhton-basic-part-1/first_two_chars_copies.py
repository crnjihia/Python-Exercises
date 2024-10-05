def first_two_copies(s, n):
    if len(s) < 2:
        return s * n
    return s[:2] * n

print(first_two_copies("hello", 3))
