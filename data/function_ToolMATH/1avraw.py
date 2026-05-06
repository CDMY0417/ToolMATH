def rotate_point_i(x: float, y: float, angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    new_x = x * math.cos(angle_radians) - y * math.sin(angle_radians)
    new_y = x * math.sin(angle_radians) + y * math.cos(angle_radians)
    return new_x, new_y
