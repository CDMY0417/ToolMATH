def complete_the_square_ar(a: float, b: float, c: float) -> tuple:
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return (h, k)
