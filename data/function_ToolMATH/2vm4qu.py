def complete_square_b(a: int, b: int):
    h = b / (2 * a)
    k = a * h ** 2
    return f'({a}*(x + {h})**2)', k
