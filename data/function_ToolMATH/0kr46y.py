def simplify_fraction_b(numerator: int, denominator: int) -> tuple:
    from math import gcd
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)
