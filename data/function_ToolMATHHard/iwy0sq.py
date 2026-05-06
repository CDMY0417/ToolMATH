def b_from_cubic_factor_quadratic(p: float):
    """Return b from factorization (x^2+px+1)(2x+q)."""
    q = 7  # from constant term 1*q=7
    # Compare coefficients: (x^2+px+1)(2x+q) => b = p*q + 2
    return p*q + 2
