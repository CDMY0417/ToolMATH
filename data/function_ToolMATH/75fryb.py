def gcd_g(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return abs(x)
