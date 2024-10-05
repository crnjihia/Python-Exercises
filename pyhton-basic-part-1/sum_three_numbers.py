def sum_three_numbers(a, b, c):
    total = a + b + c
    if a == b == c:
        return total * 3
    return total

print(sum_three_numbers(1, 2, 3))
