def cis_form(modulus: float, angle_degrees: float):
    import cmath
    angle_radians = cmath.pi * angle_degrees / 180
    return modulus * (cmath.cos(angle_radians) + 1j * cmath.sin(angle_radians))
