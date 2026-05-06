def distance_from_center(center: tuple, radius: float, angle: float):
    from math import cos, sin
    x_center, y_center = center
    x = x_center + radius * cos(angle)
    y = y_center + radius * sin(angle)
    return (x, y)
