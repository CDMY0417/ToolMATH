def rotation_matrix_b(angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    cos_theta = math.cos(angle_radians)
    sin_theta = math.sin(angle_radians)
    return [[cos_theta, -sin_theta], [sin_theta, cos_theta]]
