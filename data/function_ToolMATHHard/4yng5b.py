def circle_radius_from_standard_coeffs(D: float, E: float, F: float):
    """Return radius r for x^2 + y^2 + D*x + E*y + F = 0."""
    r_sq = (D/2.0)**2 + (E/2.0)**2 - F
    if r_sq < 0:
        raise ValueError("Radius squared is negative.")
    return r_sq ** 0.5
