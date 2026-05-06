import cmath
import math

def cis_to_complex(r: float, theta_degrees: float) -> complex:
    theta_radians = math.radians(theta_degrees)
    return r * cmath.rect(1, theta_radians)
