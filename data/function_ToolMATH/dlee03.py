def count_multiples_in_range_g(multiple: int, low: int, high: int) -> int:
    if low % multiple == 0:
        start = low
    else:
        start = low + (multiple - low % multiple)
    if high % multiple == 0:
        end = high
    else:
        end = high - high % multiple
    if start > end:
        return 0
    return (end - start) // multiple + 1
