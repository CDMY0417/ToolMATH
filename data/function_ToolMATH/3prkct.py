def longer_segment_length(total_length: float, ratio_part1: int, ratio_part2: int):
    return (total_length * max(ratio_part1, ratio_part2)) / (ratio_part1 + ratio_part2)
