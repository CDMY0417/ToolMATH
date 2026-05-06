def exclude_value_from_range(excluded_value: float):
    return ((float('-inf'), excluded_value), (excluded_value, float('inf')))
