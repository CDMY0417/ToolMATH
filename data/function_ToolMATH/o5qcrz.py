def is_relatively_prime_b(a: int, b: int) -> bool:
    from math import gcd
    return gcd(a, b) == 1
