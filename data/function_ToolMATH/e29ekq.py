def increase_side_lengths(sides: list[float], percent: float) -> list[float]:
    return [side * (1 + percent / 100) for side in sides]
