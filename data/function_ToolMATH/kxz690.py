def probability_as_fraction_c(successful: int, total: int) -> str:
    from math import gcd
    g = gcd(successful, total)
    return f'{successful // g}/{total // g}'
