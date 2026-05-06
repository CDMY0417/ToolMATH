def gcd_ch(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
