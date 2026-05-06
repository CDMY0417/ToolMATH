def angle_between_vectors_a(a_dot_c: float, norm_a: float, norm_c: float) -> float:
    from math import acos, degrees
    cos_theta = a_dot_c / (norm_a * norm_c)
    angle_rad = acos(min(1, max(-1, cos_theta)))  # Ensure the value is in [-1, 1] range
    return degrees(angle_rad)
