def complete_square_p(a: int, b: int):
    h = -b / (2 * a)
    k = (b ** 2) / (4 * a)
    return h, k
