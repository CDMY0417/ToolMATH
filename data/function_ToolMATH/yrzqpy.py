def probability_all_events(probabilities: list[float]) -> float:
    result = 1.0
    for prob in probabilities:
        result *= prob
    return result
