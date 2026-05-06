def shifted_square_to_linear_coeffs(shift: float):
    """Return (A,B) such that A*x + B = 0 is equivalent to (x+shift)^2 = x^2."""
    return (2.0*shift, shift**2)
