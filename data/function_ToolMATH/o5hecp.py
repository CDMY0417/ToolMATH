def greatest_value_below_limit(values: list[int], limit: int):
    return max(value for value in values if value < limit)
