def complete_the_square_k(a: float, b: float):
    h = b / (2 * a)
    k = -a * h ** 2
    return h, k
