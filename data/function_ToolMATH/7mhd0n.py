def cosine_of_angle_in_unit_circle(angle_degrees: float) -> float:
    import math
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
    # Compute x-coordinate of point on unit circle
    x = math.cos(angle_radians)
    return x
