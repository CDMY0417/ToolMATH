def simplify_fraction_d(numerator: int, denominator: int) -> tuple:
    from math import gcd
    factor = gcd(numerator, denominator)
    return (numerator // factor, denominator // factor)
