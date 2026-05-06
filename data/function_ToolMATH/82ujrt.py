def probability_of_both_getting_same_number(probabilities: list[float]) -> float:
    return sum(p ** 2 for p in probabilities)
