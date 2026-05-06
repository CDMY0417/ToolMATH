def lcm_j(a: int, b: int):
    from math import gcd
    return abs(a * b) // gcd(a, b)
