def simplify_fraction_ao(numerator: int, denominator: int) -> tuple:
    import math
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd
