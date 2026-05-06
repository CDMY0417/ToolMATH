def divide_complex_numbers(a: float, b: float, c: float, d: float):
    """Return (a+bi)/(c+di) as complex."""
    denom = c * c + d * d
    if denom == 0:
        raise ValueError("Denominator is zero.")
    real = (a * c + b * d) / denom
    imag = (b * c - a * d) / denom
    return complex(real, imag)
