def sum_and_round_to_nearest_ten(numbers: list[int]) -> int:
    total = sum(numbers)
    return round(total, -1)
