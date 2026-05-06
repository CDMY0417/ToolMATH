def invert_complex_number(a: float, b: float):
    denominator = a**2 + b**2
    real_part = a / denominator
    imaginary_part = -b / denominator
    return real_part, imaginary_part
