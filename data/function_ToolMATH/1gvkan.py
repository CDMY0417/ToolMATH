def units_digit_of_power(base: int, exponent: int):
    units_cycle = []
    current = base % 10
    while current not in units_cycle:
        units_cycle.append(current)
        current = (current * base) % 10
    cycle_length = len(units_cycle)
    return units_cycle[(exponent - 1) % cycle_length]
