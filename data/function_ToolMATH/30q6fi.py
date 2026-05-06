def digit_sum_pairs(target_sum: int, first_digit: int):
    pairs = []
    for i in range(10):
        if 0 <= target_sum - first_digit - i < 10:
            pairs.append((i, target_sum - first_digit - i))
    return pairs
