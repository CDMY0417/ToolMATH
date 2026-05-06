def probability_sequence(probabilities: list[float]) -> float:
    from functools import reduce
    from operator import mul
    return reduce(mul, probabilities, 1)
