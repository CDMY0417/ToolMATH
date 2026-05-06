def vector_magnitude_a(vector: list[float]) -> float:
    return sum(x**2 for x in vector) ** 0.5
