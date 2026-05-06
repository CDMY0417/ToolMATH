def rectangular_to_spherical(x: float, y: float, z: float):
    import math
    rho = math.sqrt(x**2 + y**2 + z**2)
    phi = math.acos(z / rho)
    theta = math.atan2(y, x)
    return (rho, theta, phi)
