def is_relatively_prime(x: int, y: int) -> bool:
    from math import gcd
    return gcd(x, y) == 1
