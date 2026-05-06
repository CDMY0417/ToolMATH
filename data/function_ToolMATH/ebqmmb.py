def constant_term_of_polynomial_a(roots: list[int]) -> int:
    constant_term = 1
    for root in roots:
        constant_term *= root
    return constant_term
