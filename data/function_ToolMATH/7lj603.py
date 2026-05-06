def complete_square_d(a: int, b: int) -> tuple:
    h = -b / (2 * a)
    k = a * h * h
    return h, k
