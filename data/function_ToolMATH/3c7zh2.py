def area_of_isosceles_triangle_b(side_length: float, angle_degrees: float):
    import math
    area = 0.5 * side_length**2 * math.sin(math.radians(angle_degrees))
    return area
