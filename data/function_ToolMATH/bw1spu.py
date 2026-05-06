def subtract_complex_numbers(complex1: tuple[float, float], complex2: tuple[float, float]) -> tuple[float, float]:
    real_part = complex1[0] - complex2[0]
    imag_part = complex1[1] - complex2[1]
    return (real_part, imag_part)
