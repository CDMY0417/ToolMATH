def units_digit_of_power_b(base: int, exponent: int) -> int:
    units_digit = base % 10
    if units_digit == 9:
        return 9 if exponent % 2 == 1 else 1
    else:
        cycle = [(units_digit ** i) % 10 for i in range(1, 5)]
        return cycle[(exponent - 1) % len(cycle)]
