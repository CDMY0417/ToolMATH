def find_units_digit_of_power(a: int, n: int) -> int:
    cycle = []
    current = a
    seen = set()
    while current % 10 not in seen:
        seen.add(current % 10)
        cycle.append(current % 10)
        current *= a
    return cycle[(n - 1) % len(cycle)]
