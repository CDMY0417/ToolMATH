def line_parameterization_a(point1: tuple[float, float], point2: tuple[float, float], t: float) -> tuple[float, float]:
    direction_vector = (point2[0] - point1[0], point2[1] - point1[1])
    line_point = (point1[0] + t * direction_vector[0], point1[1] + t * direction_vector[1])
    return line_point
