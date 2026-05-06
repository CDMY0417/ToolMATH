def sum_excluding_value(values: list[int], exclude: int) -> int:
    return sum(x for x in values if x != exclude)
