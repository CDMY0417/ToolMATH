def expand_binomial_product(a: int, b: int, c: int, d: int, e: int):
    A = a * c
    B = a * d + b * c
    C = a * e + b * d
    D = b * e
    return A, B, C, D
