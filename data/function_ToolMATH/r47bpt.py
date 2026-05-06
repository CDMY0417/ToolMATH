def complete_square_w(a: float, b: float):
    h = -b / (2 * a)
    return h, a * h**2 + b * h
