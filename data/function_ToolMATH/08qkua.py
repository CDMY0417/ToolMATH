def parameterize_line_a(point: list[float], direction: list[float], t: float) -> list[float]:
    return [p + t * d for p, d in zip(point, direction)]
