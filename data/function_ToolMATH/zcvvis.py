def divide_complex_numbers(a1: float, b1: float, a2: float, b2: float):
    denominator = a2**2 + b2**2
    real_part = (a1 * a2 + b1 * b2) / denominator
    imag_part = (b1 * a2 - a1 * b2) / denominator
    return real_part, imag_part
