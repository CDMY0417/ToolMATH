def simplify_fraction_o(numerator: int, denominator: int):
    from math import gcd
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value, denominator // gcd_value
