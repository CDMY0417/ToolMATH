import math

def distance_between_ellipse_foci(a: float, b: float):
    # Distance between foci for ellipse x^2/a^2 + y^2/b^2 = 1 (a>=b)
    c = math.sqrt(a*a - b*b)
    return 2*c
