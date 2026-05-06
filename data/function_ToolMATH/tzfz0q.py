def round_up(number: float) -> int:
    return int(number) + (1 if number % 1 > 0 else 0)
