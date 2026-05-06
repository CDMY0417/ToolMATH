def probability_of_consecutive_independent_events(probability_single_event: float, number_of_events: int) -> float:
    probability = probability_single_event ** number_of_events
    return probability
