def solve_equations(target_sum: float, proportions: list[float]) -> list[float]:
    scale = target_sum / sum(proportions)
    return [p * scale for p in proportions]
