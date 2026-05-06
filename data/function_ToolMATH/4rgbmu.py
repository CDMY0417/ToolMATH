def add_polynomials_a(poly1: list[int], poly2: list[int]) -> list[int]:
    # Extend the shorter polynomial with zeros
    if len(poly1) < len(poly2):
        poly1 = poly1 + [0] * (len(poly2) - len(poly1))
    elif len(poly2) < len(poly1):
        poly2 = poly2 + [0] * (len(poly1) - len(poly2))
    # Add corresponding coefficients
    result = [a + b for a, b in zip(poly1, poly2)]
    return result
