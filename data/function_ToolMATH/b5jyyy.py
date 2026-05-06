def gcd_euclidean_c(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
