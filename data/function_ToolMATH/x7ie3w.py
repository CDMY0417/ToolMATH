def multiply_complex_numbers_d(a: int, b: int, c: int, d: int):
    real_part = a * c - b * d
    imaginary_part = a * d + b * c
    return real_part, imaginary_part
