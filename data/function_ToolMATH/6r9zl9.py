def reduce_fraction_c(numerator: int, denominator: int) -> (int, int):
    from math import gcd
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor
