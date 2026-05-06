def spherical_to_rectangular(rho: float, theta: float, phi: float):
    import math
    x = rho * math.sin(phi) * math.cos(theta)
    y = rho * math.sin(phi) * math.sin(theta)
    z = rho * math.cos(phi)
    return (x, y, z)
