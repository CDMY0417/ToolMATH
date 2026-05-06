def lcm_g(a: int, b: int):
    from math import gcd
    return abs(a * b) // gcd(a, b)
