def vector_difference(v1: list[float], v2: list[float]) -> list[float]:
    return [a - b for a, b in zip(v1, v2)]
