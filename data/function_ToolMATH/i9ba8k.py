def spherical_to_rectangular_x(rho: float, theta: float, phi: float) -> float:
    from math import sin, cos
    return rho * sin(phi) * cos(theta)
