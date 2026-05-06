def opposite_face_pairs(n: int):
    opposite_pairs = []
    for i in range(1, n//2 + 1):
        opposite_pairs.append((i, n + 1 - i))
    return opposite_pairs
