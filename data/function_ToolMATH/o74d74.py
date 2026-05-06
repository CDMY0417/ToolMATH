def calculate_probabilities(total: int, event_count: int):
    prob_event = event_count / total
    prob_other = (total - event_count) / total
    return prob_event, prob_other
