def adjust_multiple_counts(total_count: int, duplicated_count: int, occurrences: int) -> int:
    return total_count - (occurrences - 1) * duplicated_count
