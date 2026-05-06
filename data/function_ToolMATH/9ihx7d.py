def even_numbers_in_range(start: int, end: int) -> list:
    return [n for n in range(start, end + 1) if n % 2 == 0]
