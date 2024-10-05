def sum_with_conditions(a, b, c):
    if a == b or b == c or a == c:
        return 0
    return a + b + c

print("Sum:", sum_with_conditions(5, 5, 3))
