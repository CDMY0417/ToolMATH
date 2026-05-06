def sum_pairs_for_target(sides: int, target: int) -> list:
    pairs = []
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            if i + j == target:
                pairs.append((i, j))
    return pairs
