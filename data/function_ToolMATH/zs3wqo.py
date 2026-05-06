def gcd_cb(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
