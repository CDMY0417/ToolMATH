def parallelogram_area_from_vectors(vector_a: tuple[float, float], vector_b: tuple[float, float]) -> float:
    return abs(vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0])
