def find_integer_bound(value: float) -> int:
    return int(value) if value > int(value) else int(value) - 1
