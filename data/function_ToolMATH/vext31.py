def complete_the_square_as(a: int, b: int):
    h = b / (2 * a)
    k = a * h * h
    return a, h, k
