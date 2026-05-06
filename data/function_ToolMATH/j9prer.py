def least_common_multiple_condition(val: int, mult: int, low: int, high: int) -> bool:
    return low <= val <= high and val % mult == 0
