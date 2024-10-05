def calculate_future_value(principal, rate, years):
    future_value = principal * (1 + rate / 100) ** years
    print(f"Future value: {future_value:.2f}")

calculate_future_value(10000, 3.5, 7)
