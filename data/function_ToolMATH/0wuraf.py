def reduce_fraction_a(numerator: int, denominator: int):
    from math import gcd
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor
