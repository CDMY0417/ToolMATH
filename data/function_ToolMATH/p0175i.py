def average_of_numbers_f(numbers: list[float]) -> float:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
