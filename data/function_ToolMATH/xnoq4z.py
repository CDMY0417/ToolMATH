def reduce_fraction_i(numerator: int, denominator: int) -> tuple:
    from math import gcd
    gcd_value = gcd(numerator, denominator)
    return (numerator // gcd_value, denominator // gcd_value)
