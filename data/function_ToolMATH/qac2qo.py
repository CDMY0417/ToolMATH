def distribute_complex_a(complex1: tuple[float, float], complex2: tuple[float, float]) -> tuple[float, float]:
    real1, imag1 = complex1
    real2, imag2 = complex2
    real = real1 * real2 - imag1 * imag2
    imag = real1 * imag2 + imag1 * real2
    return (real, imag)
