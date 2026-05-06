def rotate_point_d(point: tuple[float, float], angle_degrees: float) -> tuple[float, float]:
    import math
    angle_radians = math.radians(angle_degrees)
    x, y = point
    x_rotated = x * math.cos(angle_radians) - y * math.sin(angle_radians)
    y_rotated = x * math.sin(angle_radians) + y * math.cos(angle_radians)
    return (x_rotated, y_rotated)
