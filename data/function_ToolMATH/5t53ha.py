def gcd_e(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
