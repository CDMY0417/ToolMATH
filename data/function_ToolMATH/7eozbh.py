def simplify_ratio_b(a: int, b: int):
    from math import gcd
    common_divisor = gcd(a, b)
    return (a // common_divisor, b // common_divisor)
