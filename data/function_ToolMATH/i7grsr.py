def calculate_mode(data: list[int]) -> int:
    from collections import Counter
    count = Counter(data)
    mode = count.most_common(1)[0][0]
    return mode
