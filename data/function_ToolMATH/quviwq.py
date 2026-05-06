def vector_addition_c(vec1: list[float], vec2: list[float]) -> list[float]:
    return [x + y for x, y in zip(vec1, vec2)]
