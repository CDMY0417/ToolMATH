def calculate_mode_b(numbers: list[int]) -> int:
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    mode = [num for num, freq in count.items() if freq == max_count]
    return mode[0] if len(mode) == 1 else None
