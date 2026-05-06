def square_complex_number(real: int, imaginary: int):
    real_part = real * real - imaginary * imaginary
    imaginary_part = 2 * real * imaginary
    return real_part, imaginary_part
