def subtract_sequence(start: int, numbers: list[int]) -> int:
    for number in numbers:
        start -= number
    return start
