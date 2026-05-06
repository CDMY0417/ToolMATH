def point_on_unit_circle(angle_degrees: float) -> tuple:
    import math
    angle_radians = math.radians(angle_degrees)
    x = math.cos(angle_radians)
    y = math.sin(angle_radians)
    return (x, y)
