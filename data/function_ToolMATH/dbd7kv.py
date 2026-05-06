def simplify_fraction_s(numerator: int, denominator: int):
    from math import gcd
    gcd_val = gcd(numerator, denominator)
    return (numerator // gcd_val, denominator // gcd_val)
