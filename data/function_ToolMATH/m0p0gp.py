def probability_fraction_a(events: int, total: int) -> tuple:
    from math import gcd
    common_divisor = gcd(events, total)
    return (events // common_divisor, total // common_divisor)
