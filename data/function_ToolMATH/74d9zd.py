def probability_of_successive_events(successes: list[int], total_possibilities: list[int]) -> float:
    probability = 1.0
    for success, total in zip(successes, total_possibilities):
        probability *= success / total
    return probability
