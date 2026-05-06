def simplify_fraction(numerator: int, denominator: int) -> tuple:
    from math import gcd
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
