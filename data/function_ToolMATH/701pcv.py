def rotate_vector_counterclockwise(angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    return [[math.cos(angle_radians), -math.sin(angle_radians)],
            [math.sin(angle_radians), math.cos(angle_radians)]]
