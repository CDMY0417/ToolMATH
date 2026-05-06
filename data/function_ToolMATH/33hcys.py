def gcd_using_euclidean_algorithm(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
