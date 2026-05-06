def expand_square_terms(numbers: list[float]) -> float:
    expanded_sum = sum((x - 1)**2 for x in numbers)
    return expanded_sum
