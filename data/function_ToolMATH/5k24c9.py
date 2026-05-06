def cartesian_to_polar_distance(x: float, y: float):
    from math import sqrt, atan2
    r = sqrt(x ** 2 + y ** 2)
    theta = atan2(y, x)
    return r, theta
