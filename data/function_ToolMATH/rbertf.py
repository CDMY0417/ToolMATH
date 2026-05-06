def circumradius_from_sine_law(bc: float, angle_a_degrees: float) -> float:
    import math
    angle_a_radians = math.radians(angle_a_degrees)
    return bc / (2 * math.sin(angle_a_radians))
