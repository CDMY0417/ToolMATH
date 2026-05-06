def multiples_in_range_f(start: int, end: int, multiple: int):
    return [x for x in range(start, end + 1) if x % multiple == 0]
