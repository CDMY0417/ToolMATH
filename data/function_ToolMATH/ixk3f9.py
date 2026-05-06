def squared_vector_difference(v1: list[float], scale1: float, v2: list[float], scale2: float) -> float:
    diff = [(scale1 * x1) - (scale2 * x2) for x1, x2 in zip(v1, v2)]
    return sum(x ** 2 for x in diff)
