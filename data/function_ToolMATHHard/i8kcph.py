import math

def spherical_to_x_plus_z(rho: float, theta: float, phi: float):
    x = rho*math.sin(phi)*math.cos(theta)
    z = rho*math.cos(phi)
    return x + z
