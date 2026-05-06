def gcd_ay(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
