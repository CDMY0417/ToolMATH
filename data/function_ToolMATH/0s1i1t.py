from math import acos, degrees

def angle_between_vectors_degrees(dot_product: float, magnitude_a: float, magnitude_b: float):
    cos_theta = dot_product / (magnitude_a * magnitude_b)
    theta = acos(cos_theta)
    return degrees(theta)
