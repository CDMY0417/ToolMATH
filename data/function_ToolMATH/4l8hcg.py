def weighted_probability_a(probabilities: list) -> float:
    selection_probability = 1 / len(probabilities)
    total_probability = 0
    for probability in probabilities:
        total_probability += selection_probability * probability
    return total_probability
