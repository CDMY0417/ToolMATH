def complete_the_square_m(a: float, b: float, c: float):
    h = b / (2 * a)
    k = c - a * h**2
    return (a, h, k)
