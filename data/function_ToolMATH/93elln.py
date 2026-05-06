def gcd_euclidean_g(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
