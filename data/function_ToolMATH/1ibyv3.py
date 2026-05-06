def solve_ratio_equation_b(ratios: list[float], total_sum: float) -> float:
    x_coefficient = sum(ratios)
    return total_sum / x_coefficient
