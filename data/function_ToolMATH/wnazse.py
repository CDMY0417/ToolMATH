import math
def create_rotation_matrix(theta: float) -> list[list[float]]:
    return [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
