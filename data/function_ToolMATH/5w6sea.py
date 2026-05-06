def substitute_parametric_line(point: list[float], direction: list[float], parameter: float) -> list[float]:
    return [p + parameter * d for p, d in zip(point, direction)]
