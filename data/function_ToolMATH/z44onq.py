import math
def tangent_a(angle_degrees: float) -> float:
    radians = math.radians(angle_degrees)
    return math.sin(radians) / math.cos(radians)
