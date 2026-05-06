def generate_even_integers(start: int, end: int) -> list:
    return [n for n in range(start, end + 1) if n % 2 == 0]
