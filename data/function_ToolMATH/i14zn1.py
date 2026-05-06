def probability_no_match(n: int, sides: int) -> float:
    probability = 1.0
    for i in range(n):
        probability *= (sides - i) / sides
    return probability
