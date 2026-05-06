def median_from_histogram(frequencies: list[int], total_items: int) -> int:
    cumulative = 0
    target = (total_items + 1) // 2
    for i, freq in enumerate(frequencies):
        cumulative += freq
        if cumulative >= target:
            return i
    return -1
