def remove_elements_and_average(numbers: list[float], to_remove: list[float]) -> float:
    remaining_numbers = [num for num in numbers if num not in to_remove]
    return sum(remaining_numbers) / len(remaining_numbers) if remaining_numbers else 0.0
