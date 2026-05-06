def complete_square_aa(a: int, b: int):
    h = -b / (2 * a)
    k = a * h**2 + b * h
    return h, k
