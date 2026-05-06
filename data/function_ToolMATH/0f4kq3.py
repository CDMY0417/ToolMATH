def complete_square(a: int, b: int) -> tuple:
    h = -b / (2 * a)
    k = a * h**2 + b * h
    return (h, k)
