def probability_not_occurring(probabilities: list[float]) -> float:
    prob_not_occurring = 1.0
    for p in probabilities:
        prob_not_occurring *= (1 - p)
    return prob_not_occurring
