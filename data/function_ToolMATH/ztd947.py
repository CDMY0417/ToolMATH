def product_pos_int_pairs(target: int):
    pairs = []
    for i in range(1, int(target**0.5) + 1):
        if target % i == 0:
            pairs.append((i, target // i))
    return pairs
