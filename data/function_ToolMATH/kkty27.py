def gcd_bc(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
