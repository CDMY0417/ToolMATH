def probability_of_event_ax(event_probs: list[float]) -> float:
    from functools import reduce
    from operator import mul
    return reduce(mul, event_probs)
