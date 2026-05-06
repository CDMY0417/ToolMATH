def complete_square_h(a: int, b: int):
    h = b / (2 * a)
    k = a * h**2
    return (h, k)
