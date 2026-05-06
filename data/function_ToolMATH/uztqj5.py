def units_digit_e(base: int, exponent: int) -> int:
    cycle = []
    current = base % 10
    while current not in cycle:
        cycle.append(current)
        current = (current * base) % 10
    return cycle[(exponent - 1) % len(cycle)]
