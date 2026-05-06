def smallest_integer_greater_than(value: float) -> int:
    return int(value) + 1 if not value.is_integer() else int(value)
