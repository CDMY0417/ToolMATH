def coordinates_on_unit_circle_b(angle_degrees: float) -> tuple:
    import math
    radians = math.radians(angle_degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
