def check_equal_sum_difference(a, b):
    return a == b or abs(a - b) == 5 or (a + b) == 5

print("Condition met:", check_equal_sum_difference(10, 5))
