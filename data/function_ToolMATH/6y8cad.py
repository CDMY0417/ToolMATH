def simplify_fraction_f(numerator_denominator: tuple) -> tuple:
    from math import gcd
    numerator, denominator = numerator_denominator
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
