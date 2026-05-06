def find_minimum_integer_greater_than(value: float) -> int:
    return int(value) + 1 if value != int(value) else int(value)
