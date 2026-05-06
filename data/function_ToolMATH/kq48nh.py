def median(sorted_numbers: list[float]) -> float:
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
