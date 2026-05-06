def gcd_t(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
