def distance_in_unit_circle_for_angle(angle_degrees: float):
    import math
    radians = math.radians(angle_degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
