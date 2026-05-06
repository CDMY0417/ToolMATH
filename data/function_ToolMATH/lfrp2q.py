def sum_of_integers_to_pairs(total: int):
    pairs = []
    for i in range(1, total):
        pairs.append((i, total - i))
    return pairs
