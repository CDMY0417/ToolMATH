def are_direction_vectors_equivalent(vector1: tuple[float, float], vector2: tuple[float, float]) -> bool:
    if vector1[0] == 0 or vector2[0] == 0:
        return vector1[0] == 0 and vector2[0] == 0 and vector1[1] == 0 and vector2[1] == 0
    return vector1[0] * vector2[1] == vector1[1] * vector2[0]
