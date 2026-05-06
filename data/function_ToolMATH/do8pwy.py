def gcd_multiple_numbers(a: int, b: int, c: int) -> int:
    from math import gcd
    return gcd(gcd(a, b), c)
