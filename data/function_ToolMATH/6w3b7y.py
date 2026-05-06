def probability_of_correct_guesses(probabilities: list[float]) -> float:
    probability = 1.0
    for p in probabilities:
        probability *= p
    return probability
