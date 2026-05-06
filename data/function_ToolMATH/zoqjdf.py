def lcm_m(a: int, b: int) -> int:
    from math import gcd
    return a * b // gcd(a, b)
