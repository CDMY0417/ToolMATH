def independent_event_probability_a(probabilities: list[float]) -> float:
    probability = 1.0
    for p in probabilities:
        probability *= p
    return probability
