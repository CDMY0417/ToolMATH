def simplify_fraction_m(numerator: int, denominator: int):
    import math
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd
