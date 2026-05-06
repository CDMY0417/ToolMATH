def digit_pairs_with_ratio(multiple: int):
    pairs = [(a, b) for a in range(1, 10) for b in range(1, 10) if a == multiple * b]
    return pairs
