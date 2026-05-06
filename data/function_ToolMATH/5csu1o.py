def successive_probability(counts: list[int]) -> float:
    probability = 1
    total = sum(counts)
    for available in counts:
        probability *= available / total
        total -= 1
    return probability
