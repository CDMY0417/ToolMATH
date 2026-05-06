def fraction_remaining_after_reductions(reductions: list[float]) -> float:
    remaining_fraction = 1.0
    for reduction in reductions:
        remaining_fraction *= reduction
    return remaining_fraction
