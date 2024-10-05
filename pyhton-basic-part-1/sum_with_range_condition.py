def sum_with_range_condition(a, b):
    total = a + b
    if 15 <= total <= 20:
        return 20
    return total

print("Result:", sum_with_range_condition(10, 7))
