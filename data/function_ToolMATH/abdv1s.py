def parallelogram_area(vector1: tuple[float, float], vector2: tuple[float, float]) -> float:
    return abs(vector1[0] * vector2[1] - vector1[1] * vector2[0])
