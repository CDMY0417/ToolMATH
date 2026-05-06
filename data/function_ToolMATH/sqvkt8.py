def complete_the_square_v(a: float, b: float) -> tuple:
    h = -b / (2 * a)
    k = a * h**2 + b * h
    return h, k
