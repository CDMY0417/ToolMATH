def gcd_bo(a: int, b: int):
    while b:
        a, b = b, a % b
    return a
