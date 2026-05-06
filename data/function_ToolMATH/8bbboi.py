def expand_binomial_product_f(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    A = a1 * a2
    B = a1 * b2 + b1 * a2
    C = a1 * c2 + b1 * b2 + c1 * a2
    D = b1 * c2 + c1 * b2
    E = c1 * c2
    return (A, B, C, D, E)
