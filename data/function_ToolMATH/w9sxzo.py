def gcd_euclidean_algorithm_b(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
