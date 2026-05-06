def find_divisibles_in_range(start: int, end: int, divisor: int) -> list:
    return [n for n in range(start, end + 1) if n % divisor == 0]
