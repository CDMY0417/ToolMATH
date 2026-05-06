def count_boxes_above_threshold(values: list[float], threshold: float) -> int:
    count = sum(1 for value in values if value >= threshold)
    return count
