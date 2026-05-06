def expected_value_f(probabilities: list[float], outcomes: list[float]) -> float:
    return sum(p * o for p, o in zip(probabilities, outcomes))
