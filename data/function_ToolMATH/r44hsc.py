def ceiling_of_subtracted_half(number: float) -> int:
    return int(number) if number - int(number) < 0.5 else int(number) + 1
