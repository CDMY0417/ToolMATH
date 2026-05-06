def probability_of_event_o(successful: int, total: int) -> float:
    return successful / total if total > 0 else 0
