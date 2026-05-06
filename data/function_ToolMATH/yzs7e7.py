def vector_magnitude_d(vector: list[float]) -> float:
    return sum(x**2 for x in vector) ** 0.5
