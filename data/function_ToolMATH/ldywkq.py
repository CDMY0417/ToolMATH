def quadratic_term_coefficient(poly1: list[int], poly2: list[int]) -> int:
    a, b, c = poly1
    d, e, f = poly2
    return a*f + b*e + c*d
