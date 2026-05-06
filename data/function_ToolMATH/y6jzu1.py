def simplify_fraction_an(fraction: tuple[int, int]) -> tuple[int, int]:
    from math import gcd
    numerator, denominator = fraction
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
