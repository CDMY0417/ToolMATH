def coordinates_of_point_on_unit_circle_a(angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    x = math.cos(angle_radians)
    y = math.sin(angle_radians)
    return (x, y)
