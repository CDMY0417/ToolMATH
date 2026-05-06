def remaining_length(total_length: int, segment_lengths: list[int]) -> int:
    return total_length - sum(segment_lengths)
