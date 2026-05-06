def law_of_cosines_angle_e(a: float, b: float, c: float) -> float:
    import math
    # Calculate cosine of the angle using the Law of Cosines
    cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
    # Calculate the angle in radians
    angle_rad = math.acos(cos_angle)
    # Convert angle to degrees
    angle_deg = math.degrees(angle_rad)
    return angle_deg
