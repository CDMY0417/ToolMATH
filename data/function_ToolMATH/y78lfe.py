def vector_norm_c(vector: list[float]) -> float:
    return sum(x**2 for x in vector) ** 0.5
