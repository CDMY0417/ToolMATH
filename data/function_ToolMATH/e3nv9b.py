def count_multiples_in_range_v(multiple: int, range_start: int, range_end: int) -> int:
    return range_end // multiple - (range_start - 1) // multiple
