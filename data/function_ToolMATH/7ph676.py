def inclusion_exclusion_principle(prob_event_a: float, prob_event_b: float, prob_both_events: float) -> float:
    return prob_event_a + prob_event_b - prob_both_events
