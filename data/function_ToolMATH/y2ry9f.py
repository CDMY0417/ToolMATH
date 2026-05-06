def non_adjacent_pairs(points: list):
    n = len(points)
    pairs = []
    for i in range(n):
        for j in range(i + 2, i + n - 1):
            pairs.append((points[i], points[j % n]))
    return pairs
