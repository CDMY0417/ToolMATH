def max_and_min_difference(numbers: list[int]) -> int:
    largest = max(numbers)
    smallest = min(numbers)
    return abs(largest - smallest)
