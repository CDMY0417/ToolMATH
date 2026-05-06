def sine_of_angular_difference(angle: float, reference: float) -> float:
    import math
    return -math.sin(math.radians(angle - reference))
