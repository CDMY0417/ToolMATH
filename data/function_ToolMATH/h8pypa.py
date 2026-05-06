def angle_in_isosceles_triangle(apex_angle: float) -> tuple:
    base_angle = (180 - apex_angle) / 2
    return base_angle, base_angle, apex_angle
