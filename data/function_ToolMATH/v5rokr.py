def probability_same_number(probabilities: list[float]) -> float:
    total_probability = sum(p**2 for p in probabilities)
    return total_probability
