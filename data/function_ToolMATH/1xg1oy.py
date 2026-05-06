from math import sin, radians

def area_of_triangle_t(side1: float, side2: float, angle_degrees: float) -> float:
    angle_radians = radians(angle_degrees)
    return 0.5 * side1 * side2 * sin(angle_radians)
