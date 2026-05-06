def divisible_by(start: int, end: int, divisor: int) -> int:
    return (end // divisor) - ((start - 1) // divisor)
