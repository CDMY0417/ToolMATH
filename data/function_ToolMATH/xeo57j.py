import math

def point_on_unit_circle_a(angle_degrees: int) -> tuple:
    radians = math.radians(angle_degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
