def complete_square_coefficients(a: float, b: float, c: float):
    d = b / (2 * a)
    e = c - (b ** 2) / (4 * a)
    return d, e
