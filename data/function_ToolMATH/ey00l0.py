def digit_sum_pairs_a(digit_sum: int):
    pairs = []
    for x in range(10):
        for y in range(10):
            if x + y == digit_sum:
                pairs.append((x, y))
    return pairs
