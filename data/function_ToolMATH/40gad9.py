def common_fraction(numerator: int, denominator: int):
    from math import gcd
    divisor = gcd(numerator, denominator)
    return (numerator // divisor, denominator // divisor)
