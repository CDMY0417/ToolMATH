def group_summation(groups: list[list[float]]) -> float:
    total = 0
    for group in groups:
        total += sum(group)
    return total
