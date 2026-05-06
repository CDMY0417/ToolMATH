def cis_angle(angle_degrees: float):
    import cmath
    angle_radians = cmath.pi * angle_degrees / 180.0
    return cmath.cos(angle_radians) + cmath.sin(angle_radians) * 1j
