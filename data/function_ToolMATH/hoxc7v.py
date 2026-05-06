def simplified_fraction(numerator: int, denominator: int) -> tuple:
    from math import gcd
    divisor = gcd(numerator, denominator)
    return (numerator // divisor, denominator // divisor)
