def at_least_value(total_elements: int, size_set1: int, size_set2: int) -> int:
    return max(0, size_set1 + size_set2 - total_elements)
