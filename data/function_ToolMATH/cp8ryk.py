def sequential_divisions(numbers: list[float]) -> float:
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result
