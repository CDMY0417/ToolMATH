def cube_complex_number_a(real: int, imaginary: float):
    real_part = real**3 - 3*real*imaginary**2
    imaginary_part = 3*real**2*imaginary - imaginary**3
    return (real_part, imaginary_part)
