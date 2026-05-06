def linear_combination_complex(a_real: float, a_imag: float, b_real: float, b_imag: float, m: float, n: float):
    """Return complex number m*a + n*b."""
    real = m*a_real + n*b_real
    imag = m*a_imag + n*b_imag
    return complex(real, imag)
