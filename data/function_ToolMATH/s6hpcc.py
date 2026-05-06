def total_pairs_in_table(distance_matrix: list) -> int:
    n = len(distance_matrix)
    return n * (n - 1) // 2
