def quadratic_from_linear_terms(a: int, b: int, c: int, d: int):
    # (ax + b)(cx + d) = 0
    # Expands to acx^2 + (ad + bc)x + bd = 0
    A = a * c
    B = a * d + b * c
    C = b * d
    return A, B, C
