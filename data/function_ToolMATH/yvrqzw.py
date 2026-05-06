def complete_the_square_av(a: float, b: float):
    h = -b / (2 * a)
    k = b**2 / (4 * a)
    return (a, h, k)
