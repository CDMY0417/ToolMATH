def complete_square_form(a: float, b: float, c: float) -> tuple:
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return (h, k)
