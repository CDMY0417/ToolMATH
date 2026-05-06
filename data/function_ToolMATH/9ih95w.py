def simplify_complex_sum(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    real1, imag1 = a
    real2, imag2 = b
    real = real1 + real2
    imag = imag1 + imag2
    return (real, imag)
