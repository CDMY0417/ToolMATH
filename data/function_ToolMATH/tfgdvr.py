def multiply_complex_numbers_e(a1: float, b1: float, a2: float, b2: float):
    real_part = a1 * a2 - b1 * b2
    imag_part = a1 * b2 + b1 * a2
    return real_part, imag_part
