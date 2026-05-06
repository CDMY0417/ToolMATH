def proportional_part(part: int, part_proportion: float, total_proportion: float) -> float:
    total = part / part_proportion
    proportional_amount = total * total_proportion
    return proportional_amount
