def complete_the_square_r(a: float, b: float, c: float):
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    return (h, k)
