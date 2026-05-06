def units_digit_of_power_h(base: int, exponent: int):
    periodicity = []
    current = base % 10
    while current not in periodicity:
        periodicity.append(current)
        current = (current * base) % 10
    cycle_length = len(periodicity)
    return periodicity[(exponent - 1) % cycle_length]
