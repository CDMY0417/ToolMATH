def polar_to_rectangular(r: float, theta: float) -> complex:
    import cmath
    return r * cmath.cos(theta) + 1j * r * cmath.sin(theta)
