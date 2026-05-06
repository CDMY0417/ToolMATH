def angle_from_reflection_matrix(matrix: list[list[float]]) -> float:
    import math
    cos_2theta = matrix[0][0]
    theta_radians = math.acos(cos_2theta) / 2
    return math.degrees(theta_radians)
