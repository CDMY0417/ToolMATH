def is_invertible_modulo(a: int, m: int) -> bool:
    from math import gcd
    return gcd(a, m) == 1
