def rotation_matrix_clockwise(angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    cos_val = math.cos(angle_radians)
    sin_val = math.sin(angle_radians)
    return [[cos_val, sin_val], [-sin_val, cos_val]]
