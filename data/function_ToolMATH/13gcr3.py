def probability_of_event_within_intervals(interval_lengths: list[int], cycle_length: int) -> float:
    total_relevant_time = sum(interval_lengths)
    return total_relevant_time / cycle_length
