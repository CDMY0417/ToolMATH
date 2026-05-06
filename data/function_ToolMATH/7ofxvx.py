def find_mode(data: list[int]) -> int:
    from collections import Counter
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [val for val, count in counter.items() if count == max_count]
    return min(modes)
