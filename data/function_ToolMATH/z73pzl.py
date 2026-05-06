def probability_sequential_events(outcomes: list[float]) -> float:
    probability = 1
    for outcome in outcomes:
        probability *= outcome
    return probability
