import math

def coordinates_of_point_on_unit_circle_c(angle: float):
    radians = math.radians(angle)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
