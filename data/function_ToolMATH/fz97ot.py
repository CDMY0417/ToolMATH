def probability_of_outcomes(probabilities: list[float], occurrences: list[int]) -> float:
    from functools import reduce
    from operator import mul
    return reduce(mul, [p**o for p, o in zip(probabilities, occurrences)], 1)
