def are_vectors_parallel_a(v1: tuple[float, float, float], v2: tuple[float, float, float]) -> bool:
    if v1[0] * v2[1] != v1[1] * v2[0]:
        return False
    if v1[0] * v2[2] != v1[2] * v2[0]:
        return False
    if v1[1] * v2[2] != v1[2] * v2[1]:
        return False
    return True
