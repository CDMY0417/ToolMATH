def count_multiples_in_range_u(start: int, end: int, multiple: int) -> int:
    return len([n for n in range(start, end + 1) if n % multiple == 0])
