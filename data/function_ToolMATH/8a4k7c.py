def is_prime_square(n: int) -> bool:
    from math import isqrt
    if n < 2:
        return False
    root = isqrt(n)
    if root * root != n:
        return False
    for i in range(2, isqrt(root) + 1):
        if root % i == 0:
            return False
    return True
