def modular_simplify(a: int, b: int, m: int):
    from math import gcd
    g = gcd(a, m)
    a, b, m = a // g, b // g, m // g
    return a, b, m
