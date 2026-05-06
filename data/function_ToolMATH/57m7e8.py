def expected_value_k(probabilities: list[float], outcomes: list[float]) -> float:
    return sum(p * x for p, x in zip(probabilities, outcomes))
