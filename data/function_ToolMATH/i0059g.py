def are_relatively_prime_a(a: int, b: int, c: int) -> bool:
    from math import gcd
    return gcd(gcd(a, b), c) == 1
