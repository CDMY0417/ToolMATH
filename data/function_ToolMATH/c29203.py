def multiply_complex_numbers_a(complex1: tuple[float, float], complex2: tuple[float, float]) -> tuple[float, float]:
    a, b = complex1
    c, d = complex2
    return (a * c - b * d, a * d + b * c)
