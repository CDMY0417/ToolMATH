def multiples_in_range_c(multiple_of: int, lower_bound: int, upper_bound: int) -> int:
    start = (lower_bound + abs(lower_bound) % multiple_of) // multiple_of * multiple_of
    end = upper_bound // multiple_of * multiple_of
    if start == lower_bound:
        start += multiple_of
    if start > end:
        return 0
    return (end - start) // multiple_of + 1
