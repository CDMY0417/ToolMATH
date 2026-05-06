def complete_square_f(a: int, b: int, c: int):
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return h, k
