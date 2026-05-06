def divide_into_equal_parts(total: int, ratios: list[int]) -> float:
    sum_ratios = sum(ratios)
    return total / sum_ratios
