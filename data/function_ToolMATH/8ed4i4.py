def subtract_vectors_c(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]
