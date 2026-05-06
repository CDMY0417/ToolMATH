def convert_spherical_to_standard(rho: float, theta: float, phi: float):
    pi = 3.141592653589793
    if phi > pi:
        phi = 2 * pi - phi
        theta = theta + pi
    theta = theta % (2 * pi)
    return (rho, theta, phi)
