def rotate_point_c(x: float, y: float, theta: float):
    import math
    radians = math.radians(theta)
    new_x = x * math.cos(radians) - y * math.sin(radians)
    new_y = x * math.sin(radians) + y * math.cos(radians)
    return (new_x, new_y)
