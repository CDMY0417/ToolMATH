def complete_the_square_ab(a: int, b: int, c: int) -> tuple:
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return (h, k)
