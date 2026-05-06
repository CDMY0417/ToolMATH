def probability_event_occurs(favorable_outcomes: int, total_outcomes: int) -> float:
    if total_outcomes == 0:
        return 0.0
    return favorable_outcomes / total_outcomes
