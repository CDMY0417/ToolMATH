def direction_vectors_parallel(v1: tuple, v2: tuple) -> bool:
    if v1[0] * v2[1] == v1[1] * v2[0]:
        return True
    return False
