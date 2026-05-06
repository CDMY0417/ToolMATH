def probability_exact_combination(total_ways: int, desired_ways: int) -> float:
    if total_ways == 0:
        return 0.0
    return desired_ways / total_ways
