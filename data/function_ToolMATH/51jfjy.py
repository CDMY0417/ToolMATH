def expected_value_uniform(outcomes: list[float]) -> float:
    n = len(outcomes)
    return sum(outcomes) / n
