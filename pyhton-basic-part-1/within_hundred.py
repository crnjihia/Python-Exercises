def is_within_100(n):
    return abs(1000 - n) <= 100 or abs(2000 - n) <= 100

print(is_within_100(900))
