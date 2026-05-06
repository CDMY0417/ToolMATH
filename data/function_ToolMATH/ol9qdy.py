def complete_the_square_ai(a: float, b: float, c: float):
    h = -b / (2 * a)
    k = a * h ** 2 + b * h + c
    return (h, k)
