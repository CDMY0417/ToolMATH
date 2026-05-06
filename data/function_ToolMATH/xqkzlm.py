def solve_for_missing_probability(probabilities: list[float]) -> float:
    total_known = sum(probabilities)
    return 1 - total_known
