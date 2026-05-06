def calculate_weighted_vector_sum(weights: list[float], vectors: list[float]) -> float:
    return sum(w * v for w, v in zip(weights, vectors))
