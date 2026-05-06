def complete_the_square_j(a: int, b: int, c: int) -> tuple:
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    return (a, h, k)
