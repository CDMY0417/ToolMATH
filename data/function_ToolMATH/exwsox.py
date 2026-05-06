def gcd_be(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return abs(x)
