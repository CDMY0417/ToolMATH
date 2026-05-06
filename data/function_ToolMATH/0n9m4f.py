def polynomial_expansion(a: int) -> tuple:
    c3 = 1
    c2 = 3 * a
    c1 = 3 * a**2
    c0 = a**3
    return (c3, c2, c1, c0)
