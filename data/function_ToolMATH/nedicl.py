def complete_square_n(a: int, b: int, c: int):
    h = b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    return (a, h, k)
