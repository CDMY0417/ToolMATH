def probability_of_independent_events_b(probabilities: list[float]) -> float:
    result = 1.0
    for p in probabilities:
        result *= p
    return result
