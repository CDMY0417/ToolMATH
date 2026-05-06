def sum_reciprocal_transform(values: list[float]) -> float:
    return sum(x / (1 - x**2) for x in values if 0 < x < 1)
