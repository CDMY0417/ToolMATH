def spherical_to_rectangular_z(rho: float, phi: float) -> float:
    from math import cos
    return rho * cos(phi)
