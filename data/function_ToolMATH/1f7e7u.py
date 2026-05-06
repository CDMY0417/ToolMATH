def log_base_n(n: int, b: int) -> int:
    exponent = 0
    value = 1
    while value < n:
        value *= b
        exponent += 1
    return exponent if value == n else None
