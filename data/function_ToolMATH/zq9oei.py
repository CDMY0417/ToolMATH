def units_digit_of_power_j(a: int, b: int) -> int:
    cycle = []
    current = a % 10
    while current not in cycle:
        cycle.append(current)
        current = (current * a) % 10
    index = (b - 1) % len(cycle)
    return cycle[index]
