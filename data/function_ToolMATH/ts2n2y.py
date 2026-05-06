def rectangular_to_spherical_rho(x: float, y: float, z: float) -> float:
    from math import sqrt
    return sqrt(x**2 + y**2 + z**2)
