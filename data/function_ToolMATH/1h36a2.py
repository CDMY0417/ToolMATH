def compute_gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
