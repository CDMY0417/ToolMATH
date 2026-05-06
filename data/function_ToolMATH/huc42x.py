from numpy.polynomial import Polynomial

def polynomial_remainder(f_coeffs: list[float], g_coeffs: list[float]):
    f = Polynomial(f_coeffs)
    g = Polynomial(g_coeffs)
    remainder = f % g
    return remainder
