def complete_square_r(a: float, b: float, c: float):
    h = -b / (2 * a)
    k = c - a * (h ** 2)
    return a, h, k
