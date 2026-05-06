def normalize_vector_fraction(vector: list[float], denominator: int) -> list[int]:
    return [int(denominator * vector[i]) for i in range(len(vector))]
