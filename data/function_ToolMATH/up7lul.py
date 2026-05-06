def gcd_an(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
