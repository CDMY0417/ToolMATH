def reorder_expression_for_simplification(numbers: list[float]) -> list[float]:
    positives = [num for num in numbers if num >= 0]
    negatives = [num for num in numbers if num < 0]
    return positives + negatives
