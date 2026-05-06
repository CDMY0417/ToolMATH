def alternating_sum(numbers: list[int]) -> int:
    numbers_sorted = sorted(numbers, reverse=True)
    return sum(numbers_sorted[i] if i % 2 == 0 else -numbers_sorted[i] for i in range(len(numbers_sorted)))
