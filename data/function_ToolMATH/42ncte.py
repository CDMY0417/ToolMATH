def probability_no_successes(success_probability: float, trials: int) -> float:
    failure_probability = 1 - success_probability
    return failure_probability ** trials
