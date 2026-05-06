def gcd_ad(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)
