def coordinates_of_point_on_unit_circle(angle_degrees: float):
    import math
    x = math.cos(math.radians(angle_degrees))
    y = math.sin(math.radians(angle_degrees))
    return x, y
