def probability_all_same_color(color_count: int, total_marbles: int, k: int) -> float:
    from math import prod
    probabilities = [(color_count - i) / (total_marbles - i) for i in range(k)]
    return prod(probabilities)
