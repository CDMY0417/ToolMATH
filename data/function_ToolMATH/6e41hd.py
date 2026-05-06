def are_vectors_parallel(v1: tuple[float, float], v2: tuple[float, float]) -> bool:
    return v1[0] * v2[1] == v1[1] * v2[0]
