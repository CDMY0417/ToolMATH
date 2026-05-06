def subtract_vectors_b(vector_a: list[float], vector_b: list[float]) -> list[float]:
    return [a - b for a, b in zip(vector_a, vector_b)]
