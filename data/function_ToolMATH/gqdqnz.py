def multiples_in_range(factor: int, start: int, end: int):
    return [n for n in range(start, end + 1) if n % factor == 0]
