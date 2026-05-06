import math
def angle_between_unit_vectors(dot_product: float) -> float:
    cos_theta = dot_product / (1 * 1)  # Since they are unit vectors
    theta_radians = math.acos(cos_theta)
    return math.degrees(theta_radians)
