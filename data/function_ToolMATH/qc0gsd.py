def factor_pairs_d(integer: int):
    pairs = []
    for i in range(1, int(integer**0.5) + 1):
        if integer % i == 0:
            pairs.append((i, integer // i))
            if i != integer // i:
                pairs.append((integer // i, i))
    return pairs
