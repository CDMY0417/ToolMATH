def common_multiples_in_range(multiple: int, range_start: int, range_end: int):
    return [x for x in range(range_start + 1, range_end) if x % multiple == 0]
