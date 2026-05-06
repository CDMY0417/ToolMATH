def complete_square_aj(a: int, b: int, c: int) -> tuple:
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    return (h, k)
