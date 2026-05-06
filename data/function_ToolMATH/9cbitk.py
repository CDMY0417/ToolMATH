def get_median_of_sorted_set(numbers: list[float]) -> float:
    length = len(numbers)
    median_index = length // 2
    if length % 2 == 0:
        return (numbers[median_index - 1] + numbers[median_index]) / 2
    else:
        return numbers[median_index]
