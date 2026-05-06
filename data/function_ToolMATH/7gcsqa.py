def ones_digit_of_power_b(base: int, exponent: int):
    cycle = [base % 10]
    next_digit = (cycle[-1] * base) % 10
    while next_digit != cycle[0]:
        cycle.append(next_digit)
        next_digit = (cycle[-1] * base) % 10
    return cycle[(exponent - 1) % len(cycle)]
