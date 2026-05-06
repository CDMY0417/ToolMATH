def evaluate_monic_quartic(roots: list[float], x: float) -> float:
    result = 1
    for root in roots:
        result *= (x - root)
    return result
