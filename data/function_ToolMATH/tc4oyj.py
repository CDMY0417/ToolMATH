def complete_square_s(a: int, b: int, c: int):
    h = -b / (2 * a)
    k = (4 * a * c - b**2) / (4 * a)
    return (a, h, k)
