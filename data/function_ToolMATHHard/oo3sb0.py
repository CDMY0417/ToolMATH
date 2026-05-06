def scale_polynomial(coeffs, scalar: float):
    """Return coefficients for scalar*p(x)."""
    return [scalar*c for c in coeffs]
