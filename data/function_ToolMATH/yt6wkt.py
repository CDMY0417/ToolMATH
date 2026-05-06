def complete_the_square_ac(a: int, b: int, c: int):
    h = -b / (2 * a)
    k = (4 * a * c - b**2) / (4 * a)
    return h, k
