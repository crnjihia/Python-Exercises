def compute_lcm(a, b):
    return abs(a * b) // compute_gcd(a, b)

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("LCM of 15 and 20 is:", compute_lcm(15, 20))
