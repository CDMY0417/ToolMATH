def function_f(x: float, y: float) -> float:
    from math import sqrt
    return x * sqrt(1 - y ** 2) + y * sqrt(1 - x ** 2)
