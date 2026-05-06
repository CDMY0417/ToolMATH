def polar_distance_to_cartesian(r: float, theta: float):
    from math import cos, sin
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
