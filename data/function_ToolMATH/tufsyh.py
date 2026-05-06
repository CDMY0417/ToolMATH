def spherical_to_rectangular_y(rho: float, theta: float, phi: float) -> float:
    from math import sin
    return rho * sin(phi) * sin(theta)
