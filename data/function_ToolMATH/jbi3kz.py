def gcd_pair(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)
