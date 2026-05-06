def probability_of_exact_outcome(success_prob: float, success_count: int, failure_prob: float, failure_count: int) -> float:
    return (success_prob ** success_count) * (failure_prob ** failure_count)
