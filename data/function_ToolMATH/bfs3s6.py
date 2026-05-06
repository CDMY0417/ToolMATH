def calculate_median(numbers: list[float]) -> float:
    numbers.sort()
    n = len(numbers)
    mid_index = n // 2
    if n % 2 == 0:
        return (numbers[mid_index - 1] + numbers[mid_index]) / 2
    else:
        return numbers[mid_index]
