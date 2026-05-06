def rotation_matrix_from_theta(angle: float) -> list[list[float]]:
    import math
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return [[cos_theta, -sin_theta], [sin_theta, cos_theta]]
