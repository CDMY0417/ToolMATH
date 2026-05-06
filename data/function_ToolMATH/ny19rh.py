def coordinates_on_unit_circle_a(angle: float):
    import math
    radians = math.radians(angle)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
