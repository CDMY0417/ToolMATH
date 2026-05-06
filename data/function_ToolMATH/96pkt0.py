def multiply_complex_numbers(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    real1, imag1 = a
    real2, imag2 = b
    real_part = real1 * real2 - imag1 * imag2
    imag_part = imag1 * real2 + real1 * imag2
    return (real_part, imag_part)
