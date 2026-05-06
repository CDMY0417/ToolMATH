def gcd_bq(x: int, y: int):
    while y:
        x, y = y, x % y
    return x
