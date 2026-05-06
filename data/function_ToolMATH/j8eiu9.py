def maximum_of_quadratic(a: float, b: float, c: float) -> float:
    h = -b / (2 * a)
    return a * h ** 2 + b * h + c
