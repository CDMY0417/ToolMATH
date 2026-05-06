def multiply_complex_numbers_b(c1: tuple[float, float], c2: tuple[float, float]) -> tuple[float, float]:
    a, b = c1
    c, d = c2
    real_part = a * c - b * d
    imaginary_part = a * d + b * c
    return (real_part, imaginary_part)
