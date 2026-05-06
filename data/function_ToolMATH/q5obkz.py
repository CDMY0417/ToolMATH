def expected_value_single_day(probabilities: list[float], outcomes: list[float]) -> float:
    return sum(p * o for p, o in zip(probabilities, outcomes))
