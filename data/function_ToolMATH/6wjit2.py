def calculate_proportion_quantity(ratio: tuple[int, ...], total: int, index: int) -> int:
    factor = total // sum(ratio)
    return ratio[index] * factor
