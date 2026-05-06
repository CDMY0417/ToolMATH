def coordinates_of_point_on_circle(angle_degrees: float):
    import math
    rad = math.radians(angle_degrees)
    x = math.cos(rad)
    y = math.sin(rad)
    return (x, y)
