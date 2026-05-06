def complex_divide(a: float, b: float, c: float, d: float):
    denom = c**2 + d**2
    real = (a * c + b * d) / denom
    imag = (b * c - a * d) / denom
    return (real, imag)
