def largest_power_less_than_limit(power: int, limit: int) -> int:
    base = 1
    while (base + 1) ** power < limit:
        base += 1
    return base
