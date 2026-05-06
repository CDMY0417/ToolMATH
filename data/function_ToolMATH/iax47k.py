def probability_of_equiprobable_events(probabilities: list[float]) -> float:
    probability = 1.0
    for p in probabilities:
        probability *= p
    return probability
