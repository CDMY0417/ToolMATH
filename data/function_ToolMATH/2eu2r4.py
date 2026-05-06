import math
def cotangent(angle_degrees: float):
    radians = math.radians(angle_degrees)
    return math.cos(radians) / math.sin(radians)
