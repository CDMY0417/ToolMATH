def lcm(a: int, b: int) -> int:
    from math import gcd
    return abs(a * b) // gcd(a, b)
