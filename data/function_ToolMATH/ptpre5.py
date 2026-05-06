def solve_ratio_equation(total: int, ratios: list[int]) -> float:
    total_ratio = sum(ratios)
    x = total / total_ratio
    return x
