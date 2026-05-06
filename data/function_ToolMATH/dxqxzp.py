def cis_to_polar(angle_degrees: float) -> complex:
    import cmath
    return cmath.exp(1j * cmath.pi * angle_degrees / 180)
