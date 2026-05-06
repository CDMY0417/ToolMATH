def calculate_mean(numbers: list[float]) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
