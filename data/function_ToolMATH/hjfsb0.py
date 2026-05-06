def diametrically_opposite_point(rho: float, theta: float, phi: float):
    theta_opposite = theta + 3.141592653589793
    phi_opposite = 3.141592653589793 - phi
    return (rho, theta_opposite, phi_opposite)
