from math import comb

def probability_exactly_k_successes(success_probability: float, trials: int, k: int) -> float:
    failure_probability = 1 - success_probability
    return comb(trials, k) * (success_probability ** k) * (failure_probability ** (trials - k))
