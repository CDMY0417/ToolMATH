def simplify_fraction_bv(numerator: int, denominator: int) -> tuple[int, int]:
    from math import gcd
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
