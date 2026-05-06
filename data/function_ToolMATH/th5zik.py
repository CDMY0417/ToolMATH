def sum_pairs(n: int, target: int):
    pairs = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == target:
                pairs.append((i, j))
    return pairs
