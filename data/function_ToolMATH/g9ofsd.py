def rotate_point_on_unit_circle(degrees: float):
    import math
    radians = math.radians(degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
