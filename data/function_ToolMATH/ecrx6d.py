def expand_product_of_binomials(a1: int, b1: int, a2: int, b2: int):
    c1 = a1 * a2
    c2 = a1 * b2 + b1 * a2
    c3 = b1 * b2
    return c1, c2, c3
