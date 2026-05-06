def simplify_fraction_ai(numerator: int, denominator: int) -> tuple[int, int]:
    from math import gcd
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor
