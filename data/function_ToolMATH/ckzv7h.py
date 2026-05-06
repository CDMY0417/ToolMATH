def multiples_in_range_e(multiple: int, start: int, end: int) -> list:
    return [n for n in range(start, end + 1) if n % multiple == 0]
