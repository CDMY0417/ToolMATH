def greatest_integer_function(value: float) -> int:
    return int(value) if value >= 0 or value == int(value) else int(value) - 1
