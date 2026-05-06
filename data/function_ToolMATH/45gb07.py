def least_common_denominator(denominator1: int, denominator2: int) -> int:
    from math import gcd
    return (denominator1 * denominator2) // gcd(denominator1, denominator2)
