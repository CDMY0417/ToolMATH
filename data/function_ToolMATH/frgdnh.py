def average_of_integers_a(numbers: list[int]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
