def find_missing_value_for_mean(numbers: list[float], target_mean: float) -> float:
    existing_sum = sum(numbers)
    n = len(numbers) + 1
    total_sum_needed = target_mean * n
    return total_sum_needed - existing_sum
