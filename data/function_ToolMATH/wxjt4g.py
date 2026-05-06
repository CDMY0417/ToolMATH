def is_non_positive(a: int, b: int) -> bool:
    if b > 0:
        return a <= 0
    else:
        return a >= 0
