def complex_subtraction(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    real_part = a[0] - b[0]
    imaginary_part = a[1] - b[1]
    return (real_part, imaginary_part)
