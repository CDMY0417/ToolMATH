def generate_even_numbers_in_interval(start: int, end: int) -> list:
    return [x for x in range(start, end + 1) if x % 2 == 0]
