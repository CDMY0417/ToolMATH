def calculate_quarters_per_foot(quarters: int, height_per_stack: float) -> int:
    return int(quarters * (12 / height_per_stack))
