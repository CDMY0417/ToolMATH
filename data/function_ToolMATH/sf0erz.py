def probability_as_fraction(success: int, total: int) -> str:
    from math import gcd
    g = gcd(success, total)
    return f'{success // g}/{total // g}'
