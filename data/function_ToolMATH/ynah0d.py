def cancel_common_factors_b(numerator: int, denominator: int):
    from math import gcd
    common_factor = gcd(numerator, denominator)
    return (numerator // common_factor, denominator // common_factor)
