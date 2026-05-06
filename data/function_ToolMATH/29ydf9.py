def gcd_bn(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x
