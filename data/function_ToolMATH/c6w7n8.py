def evaluate_alternating_sum(numbers: list[int]) -> int:
    return sum((-1)**i * numbers[i] for i in range(len(numbers)))
