def simplify_fraction_bc(fraction: tuple[int, int]) -> tuple[int, int]:
    from math import gcd
    num, denom = fraction
    gcd_value = gcd(num, denom)
    return (num // gcd_value, denom // gcd_value)
