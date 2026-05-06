def relatively_prime(a: int, b: int) -> bool:
    from math import gcd
    return gcd(a, b) == 1
