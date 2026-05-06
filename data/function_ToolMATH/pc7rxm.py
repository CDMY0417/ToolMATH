def degrees_to_revolutions(degrees: int) -> tuple[int, int]:
    revolutions = degrees // 360
    remainder = degrees % 360
    return revolutions, remainder
