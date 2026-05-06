def ways_to_distribute(total_pieces: int, box_sizes: list[int]) -> int:
    ways = [1] + [0] * total_pieces
    for size in box_sizes:
        for i in range(size, total_pieces + 1):
            ways[i] += ways[i - size]
    return ways[total_pieces]
