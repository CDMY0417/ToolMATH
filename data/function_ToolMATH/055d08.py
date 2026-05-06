def pattern_of_units_digits(base: int) -> list[int]:
    units_seen = []
    current = base % 10
    while current not in units_seen:
        units_seen.append(current)
        current = (current * base) % 10
    return units_seen
