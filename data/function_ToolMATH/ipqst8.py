def arithmetic_sequence(start: int, length: int, difference: int) -> list:
    return [start + i * difference for i in range(length)]
