def gcd_bk(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
