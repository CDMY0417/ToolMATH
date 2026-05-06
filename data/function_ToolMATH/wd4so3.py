def expected_value_of_game(probabilities: list[float], values: list[float]) -> float:
    return sum(p * v for p, v in zip(probabilities, values))
