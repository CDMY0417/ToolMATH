def probability_of_event_bf(successful_outcomes: int, total_outcomes: int) -> float:
    return successful_outcomes / total_outcomes if total_outcomes > 0 else 0.0
