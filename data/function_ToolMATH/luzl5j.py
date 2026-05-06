def rotate_point_a(x: float, y: float, angle: float):
    import math
    angle_rad = math.radians(angle)
    new_x = math.cos(angle_rad) * x - math.sin(angle_rad) * y
    new_y = math.sin(angle_rad) * x + math.cos(angle_rad) * y
    return (new_x, new_y)
