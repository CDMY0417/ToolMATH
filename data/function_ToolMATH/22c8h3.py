def evaluate_division_sequence(numbers: list[float]) -> float:
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result
