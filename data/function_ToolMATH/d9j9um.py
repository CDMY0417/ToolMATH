def square_complex_number_c(real: int, imaginary: float):
    real_part = real**2 - imaginary**2
    imaginary_part = 2 * real * imaginary
    return (real_part, imaginary_part)
