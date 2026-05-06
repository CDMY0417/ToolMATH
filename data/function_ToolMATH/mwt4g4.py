def sum_of_segments_a(segment_lengths: list[int], left_length: int, right_length: int) -> int:
    return sum(segment_lengths) + left_length + right_length
