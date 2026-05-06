def complete_the_square_l(a: int, b: int, c: int):
    h = -b / (2 * a)
    k = a * h ** 2 + b * h + c
    return h, k
