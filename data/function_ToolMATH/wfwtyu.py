def vector_magnitude_squared_c(vector: dict) -> float:
    return sum(coordinate ** 2 for coordinate in vector.values())
