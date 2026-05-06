def expand_quadratic_expression_b(a: int, b: int, c: int, d: int):
    term1 = a * c
    term2 = a * d
    term3 = b * c
    term4 = b * d
    return (term1, term2 + term3, term4)
