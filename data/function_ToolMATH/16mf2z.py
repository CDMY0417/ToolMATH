def are_vectors_proportional(v1: tuple, v2: tuple) -> bool:
    if not v1 or not v2 or len(v1) != len(v2):
        return False
    ratio = [v2[i] / v1[i] if v1[i] != 0 else None for i in range(len(v1))]
    return len(set(ratio)) == 1
