def probability_fraction(favorable: int, total: int) -> str:
    from math import gcd
    common_divisor = gcd(favorable, total)
    return f'{favorable // common_divisor}/{total // common_divisor}'
