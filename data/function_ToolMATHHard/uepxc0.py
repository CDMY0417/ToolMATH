def remainder_x3_div_quadratic(p: float, q: float):
    """Return [A,B] for remainder A*x + B when dividing x^3 by x^2 + p x + q."""
    # Use reduction: x^2 = -p x - q
    # x^3 = x*(-p x - q) = -p x^2 - q x = -p(-p x - q) - q x = (p*p - q)*x + p*q
    A = p*p - q
    B = p*q
    return [A, B]
