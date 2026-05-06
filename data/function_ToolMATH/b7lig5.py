def floor_of_number_a(x: float) -> int:
    return int(x) if x == int(x) else int(x) - 1 if x < 0 else int(x)
