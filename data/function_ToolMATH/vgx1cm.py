def multiply_probabilities_a(probabilities: list[float]) -> float:
    result = 1.0
    for p in probabilities:
        result *= p
    return result
