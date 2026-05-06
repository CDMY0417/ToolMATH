def complete_the_square_au(a: int, b: int, c: int):
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return (h, k)
