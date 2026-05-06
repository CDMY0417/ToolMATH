def complex_square(z: tuple[float, float]) -> tuple[float, float]:
    real, imag = z
    real_part = real**2 - imag**2
    imag_part = 2 * real * imag
    return (real_part, imag_part)
